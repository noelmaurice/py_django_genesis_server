# variant_project API

## DO QUERIES TO THE variant_project SERVER

> This API allows to do requests to the variant_project server thanks a simple python script and without know the server structure.
>
>First to all, the python library must be imported in the python environment with the **pip install library_name** command.
>
>Then, a simple python script is enough to query the variant project server.
>
>A implementation example script for doing requests to the server is available below.

### SOURCE CODE EXAMPLE

**CAUTION: This example does not present all the possibilities of the API**

```py
import json
import os
from pprint import pprint

from anacore.annotVcf import AnnotVCFIO
from django import setup
from genesis.variant.model_data.variant import Variant

from genesis.api.variantAPI import VariantAPI

os.environ['DJANGO_SETTINGS_MODULE'] = 'genesis.api.settings'
setup()


from genesis.api.sampleAPI import SampleAPI
from genesis.sample.model_data.sample import Sample

"""
SAMPLE READ WS
"""
print('SAMPLE READ WS')
sample: Sample = SampleAPI.read(1)
print(sample.values[1]['name'], '\r\n')

"""
SAMPLE CREATE WS
"""
print('SAMPLE CREATE WS')
path_file = 'files/sample.json'
with open(path_file, 'r') as data_file:
    data_json = data_file.read()

sample_json = SampleAPI.create(data_json)
print(str(sample_json['id']), '\r\n')

"""
SAMPLE READ ALL WS
"""
print('SAMPLE READ ALL WS')
samples: [Sample] = SampleAPI.read_all()
pprint(samples[0])
print(samples[1].name, '\r\n')

"""
VARIANT CREATE WS
"""
print('VARIANT CREATE WS')
path_file = 'files/variant.json'
with open(path_file, 'r') as data_file:
    data_json = data_file.read()

variant_json: str = VariantAPI.create(data_json)
print(variant_json['id'], '\r\n')

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
VARIANT CREATE WS FROM VCF FILE
"""
print('VARIANT CREATE FROM VCF FILE WS')
reader = AnnotVCFIO('files/variants_filtered.vcf')

# variants created
for record in reader:
    samples = record.samples
    for sample in samples.items():
        variant = Variant.create(record, sample, assembly='GRCh38')
        data_json = json.dumps(variant, default=lambda o: o.__dict__)

        variant_id: [str] = []
        if variant is not None:
            variant_json: str = VariantAPI.create(data_json)
            variant_id.append(variant_json['id'])

    print(*(id for id in variant_id))
```