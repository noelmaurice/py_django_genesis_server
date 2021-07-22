# genesis API

## DO QUERIES TO THE genesis server

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

from django import setup

os.environ['DJANGO_SETTINGS_MODULE'] = 'genesis.api.settings'
setup()

from anacore.annotVcf import AnnotVCFIO

from genesis.variant.model_data.variantData import Variant
from genesis.api.variantAPI import VariantAPI
from genesis.api.sampleAPI import SampleAPI
from genesis.sample.model_data.sampleData import Sample, Part

"""
SAMPLE READ WS
"""
print('SAMPLE READ WS')
sample: Sample = SampleAPI.read(1)
print(sample.name)
print(sample.filters)
part: Part = sample.values[0]
print(part.name)
print(part.value)
print(type(sample), '\r\n')

"""
SAMPLE CREATE WS
"""
print('SAMPLE CREATE WS')
path_file = 'files/sample.json'
with open(path_file, 'r') as data_file:
    data_json = data_file.read()

id_json: str = SampleAPI.create(data_json)
print(id_json, '\r\n')

"""
SAMPLE READ ALL WS
"""
print('SAMPLE READ ALL WS')
samples: [Sample] = SampleAPI.read_all()
sample: Sample = samples[0]
print(sample.name)
print(sample.filters)
part: Part = sample.values[0]
print(part.name)
print(part.value)
print(type(sample), '\r\n')

"""
VARIANT CREATE WS
"""
print('VARIANT CREATE WS')
path_file = 'files/variant.json'
with open(path_file, 'r') as data_file:
    data_json = data_file.read()

id_json: str = VariantAPI.create(data_json)
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

        id_json: [str] = []
        if variant is not None:
            variant_json: str = VariantAPI.create(data_json)
            id_json.append(variant_json)

    print(*(id for id in id_json))
```