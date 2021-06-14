import time
from django.http import JsonResponse

from anacore.annotVcf import AnnotVCFIO
from variant.models.data.variant import Variant
from variant.models.data.parentData import DataModel
from variant.models.repository.variantRepository import VariantRepository


def index(request):
    collect = DataModel.get_collect()
    collect.remove()

    for i in range(1):
        reader = AnnotVCFIO('variant/models/files/variants_filtered.vcf')

        # variants created
        for record in reader:
            samples = record.samples
            for sample in samples.items():
                variant = Variant.create(record, sample, assembly ='GRCh38')
                if variant is not None:
                    VariantRepository.create(variant)

    data_dict = collect.find({}, {'_id': 0}).limit(3)
    data_dict = list(data_dict)

    # requests()

    # deserializing
    # data_obj = Variant.from_json(data_dict[0])
    # print(data_obj.annot[0].subject['feature'])
    # print(data_obj.coord['alt'])
    # print(data_obj.annot[0].conseq)

    return JsonResponse(data_dict, safe=False)


def requests():
    # request
    start = time.time()
    filters = VariantRepository.find_distinct_filters('splTOTO2')
    done = time.time()
    print('\r\nfind_filters -> ', round(done - start, 4))
    print(filters)

    # request
    start = time.time()
    variants = VariantRepository.find_variants_frequency('splTOTO', 40, operator='lt')
    done = time.time()
    print('\r\nfind_variant_frequencies -> ', round(done - start, 4))
    for v in variants:
        print(v)

    # request
    start = time.time()
    variants = VariantRepository.find_variants_node_value('splTOTO', 'annot.changes.HGVSc', ['524G>A'])
    done = time.time()
    print('\r\nfind_node_with_value -> ', round(done - start, 4))
    for v in variants:
        print(v)

    # request
    start = time.time()
    variants = VariantRepository.find_variants_node_value('splTOTO', 'annot.changes.HGVSp', ['ArG175HiS', 'NP_001180305'], True)
    done = time.time()
    print('\r\nfind_node_with_value -> ', round(done - start, 4))
    for v in variants:
        print(v)
    pass
