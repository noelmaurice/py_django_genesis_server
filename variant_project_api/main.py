import os
from django import setup
from variant.model_data.variant import Variant

from variant_project_api.api.variantAPI import VariantAPI

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
setup()


from variant_project_api.api.sampleAPI import SampleAPI
from sample.model_data.sample import Sample

"""
SAMPLE READ WS
"""
sample: Sample = SampleAPI.read(1)
# print(sample.values[1]['name'])

"""
SAMPLE CREATE
"""
path_file = 'api/files/sample.json'
with open(path_file, 'r') as data_file:
    data_json = data_file.read()

sample_json = SampleAPI.create(data_json)
# print(str(sample_json['id']))

"""
SAMPLE READ ALL
"""
samples: [Sample] = SampleAPI.read_all()
# pprint(samples)
# print(samples[1].name)

"""
VARIANT READ WS
"""
path_file = 'api/files/variant.json'
with open(path_file, 'r') as data_file:
    data_json = data_file.read()

variant_json: str = VariantAPI.create(data_json)
# print(variant_json['id'])

"""
VARIANT FIND NODE VALUE
"""
variants: [Variant] = VariantAPI.find_node_value("splTOTO", "annot.changes.HGVSc", "001304718")
# print(variants[0].sample_name)

"""
VARIANT FIND FILTERS
"""
filters_json: str = VariantAPI.find_distinct_filters("splTOTO")
# print(filters_json['filters'])

"""
VARIANT FIND FREQUENCY
"""
variants: [Variant] = VariantAPI.find_frequency("splTOTO", 40, 'gt')
# print(variants[0].sample_name)
