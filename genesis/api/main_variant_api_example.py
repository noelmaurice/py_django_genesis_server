import json
import os

from django import setup

os.environ['DJANGO_SETTINGS_MODULE'] = 'genesis.api.settings'
setup()

from anacore.annotVcf import AnnotVCFIO

from genesis.variant.model_data.variantData import Variant
from genesis.api.variantAPI import VariantAPI


"""
VARIANT CREATING WS
"""
print('VARIANT CREATING WS')
path_file = 'files/variant.json'
with open(path_file, 'r') as data_file:
    data_json = data_file.read()

id_json: str = VariantAPI.createWS(data_json)
print(id_json, '\r\n')

"""
VARIANT FIND NODE VALUE
"""
print('VARIANT FIND NODE VALUE WS')
variants: [Variant] = VariantAPI.find_node_value("splTOTO", "annot.changes.HGVSc", "001304718")
print(variants[0].sample_name, '\r\n')

"""
VARIANT FIND FILTERS
"""
print('VARIANT FIND FILTERS WS')
filters_json: str = VariantAPI.find_distinct_filters("splTOTO")

print(filters_json['filters'], '\r\n')

"""
VARIANT FIND FREQUENCY
"""
print('VARIANT FIND FREQUENCY WS')
variants: [Variant] = VariantAPI.find_frequency("splTOTO", 40, 'gt')
print(variants[0].sample_name, '\r\n')

"""
VARIANT CREATING WS FROM VCF FILE
"""
print('VARIANT CREATE FROM VCF FILE WS')
reader = AnnotVCFIO('files/variants_filtered.vcf')

# variants created
for record in reader:
    samples = record.samples
    for sample in samples.items():
        variant = Variant.create(record, sample, assembly='GRCh38')
        data_json = json.dumps(variant, default=lambda o: o.__dict__)

        id_json: [str] = []
        if variant is not None:
            variant_json: str = VariantAPI.createWS(data_json)
            id_json.append(variant_json)

    print(*(id for id in id_json))
