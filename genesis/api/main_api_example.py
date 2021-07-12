import json
import os
from pprint import pprint
from django import setup

os.environ['DJANGO_SETTINGS_MODULE'] = 'genesis.api.settings'
setup()

from anacore.annotVcf import AnnotVCFIO

from genesis.sample.model_data.serializers.sampleSerializer import SampleSerializer
from genesis.variant.model_data.variant import Variant

from genesis.api.variantAPI import VariantAPI


from genesis.api.sampleAPI import SampleAPI
from genesis.sample.model_data.sample import Sample, Part

"""
SAMPLE READ WS
"""
print('SAMPLE READ WS')
test: Sample = SampleAPI.test(1)
print(test.name)
print(test.pub_date)
print(test.filters)
print(Part(test.values[0]).value)
print(type(test))

# """
# SAMPLE CREATE WS
# """
# print('SAMPLE CREATE WS')
# path_file = 'files/sample.json'
# with open(path_file, 'r') as data_file:
#     data_json = data_file.read()
#
# id_json: str = SampleAPI.create(data_json)
# print(id_json, '\r\n')

# """
# SAMPLE READ ALL WS
# """
# print('SAMPLE READ ALL WS')
# samples: [Sample] = SampleAPI.read_all()
#
# pprint(samples[1])
# print(samples[0]['filters'], '\r\n')

# """
# VARIANT CREATE WS
# """
# print('VARIANT CREATE WS')
# path_file = 'files/variant.json'
# with open(path_file, 'r') as data_file:
#     data_json = data_file.read()
#
# variant_json: str = VariantAPI.create(data_json)
# variant_dict = json.loads(data_json)
# print(variant_dict['id'], '\r\n')
#
# """
# VARIANT FIND NODE VALUE
# """
# print('VARIANT FIND NODE VALUE WS')
# variants: [Variant] = VariantAPI.find_node_value("splTOTO", "annot.changes.HGVSc", "001304718")
# print(variants[0].sample_name, '\r\n')
#
# """
# VARIANT FIND FILTERS
# """
# print('VARIANT FIND FILTERS WS')
# filters_json: str = VariantAPI.find_distinct_filters("splTOTO")
#
# print(filters_json['filters'], '\r\n')
#
# """
# VARIANT FIND FREQUENCY
# """
# print('VARIANT FIND FREQUENCY WS')
# variants: [Variant] = VariantAPI.find_frequency("splTOTO", 40, 'gt')
# print(variants[0].sample_name, '\r\n')
#
# """
# VARIANT CREATE WS FROM VCF FILE
# """
# print('VARIANT CREATE FROM VCF FILE WS')
# reader = AnnotVCFIO('files/variants_filtered.vcf')
#
# # variants created
# for record in reader:
#     samples = record.samples
#     for sample in samples.items():
#         variant = Variant.create(record, sample, assembly='GRCh38')
#         data_json = json.dumps(variant, default=lambda o: o.__dict__)
#
#         variant_id: [str] = []
#         if variant is not None:
#             variant_json: str = VariantAPI.create(data_json)
#             variant_id.append(variant_json['id'])
#
#     print(*(id for id in variant_id))