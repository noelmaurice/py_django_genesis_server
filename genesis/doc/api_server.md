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

***SOURCE CODE EXAMPLE FOR VARIANT OBJECTS MANAGEMENT***

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

***SOURCE CODE EXAMPLE FOR ANALYSIS OBJECTS MANAGEMENT***

```py
import os

from django import setup

os.environ['DJANGO_SETTINGS_MODULE'] = 'genesis.api.settings'
setup()

from genesis.api.analysisAPI import *

"""
SAMPLE CREATING WS
"""
print('SAMPLE CREATING WS')

data_json = """{
        "name": "splTOTO",
        "description": "Example of sample"
        }"""

id_json: str = SampleAPI.createWS(data_json)
print(id_json, '\r\n')


"""
SAMPLE_TAG CREATING WS
"""
print('SAMPLE_TAG CREATING WS')

data_json = """{
        "key": "origin",
        "value": "anapath",
        "type": "str",
        "sample": 324
        }"""

id_json: str = SampleTagAPI.createWS(data_json)
print(id_json, '\r\n')


"""
RUN CREATING WS
"""
print('RUN CREATING WS')

data_json = """{
        "start_date": "2021-05-29 00:00:00",
        "end_date": "2021-05-30 00:00:00",
        "instrument": 18
        }"""

id_json: str = RunAPI.createWS(data_json)
print(id_json, '\r\n')

"""
RUN_TAG CREATING WS
"""
print('RUN_TAG CREATING WS')

data_json = """{
        "key": "flowcell_id",
        "value": "000000000-JHLN6",
        "type": "str",
        "run": 18
        }"""

id_json: str = RunTagAPI.createWS(data_json)
print(id_json, '\r\n')

"""
PROVIDER CREATING WS
"""
print('PROVIDER CREATING WS')

data_json = """{
        "description": "Illumina, Inc. is an American company incorporated in April 1998 that develops, manufactures and markets integrated systems for the analysis of genetic variation and biological function.",
        "name": "Illumina"
        }"""

id_json: str = ProviderAPI.createWS(data_json)
print(id_json, '\r\n')

"""
INSTRUMENT CREATING WS
"""
print('INSTRUMENT CREATING WS')

data_json = """{
        "model": "MiSeq",
        "provider_sn": "M70265",
        "category": "High-throughput sequencer",
        "provider": 19
        }"""

id_json: str = InstrumentAPI.createWS(data_json)
print(id_json, '\r\n')

"""
SOFTWARE CREATING WS
"""
print('SOFTWARE CREATING WS')

data_json = """{
        "category": "conversion",
        "description": "Conversion Software both demultiplexes data and converts BCL files generated by Illumina sequencing systems to standard FASTQ file formats for downstream analysis.",
        "name": "bcl2fastq"
        }"""

id_json: str = SoftwareAPI.createWS(data_json)
print(id_json, '\r\n')

"""
RESULT CREATING WS
"""
print('RESULT CREATING WS')

data_json = """{
        "category": "raw_reads",
        "path": "/home/toto/share/data/raw/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T019303_S1_L001_R1_001.fastq.gz",
        "type": "fastq",
        "run": 18
        }"""

id_json: str = ResultAPI.createWS(data_json)
print(id_json, '\r\n')

"""
ANALYSIS CREATING WS
"""
print('ANALYSIS CREATING WS')

data_json = """{
        "cmd": "{'R1': ['/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T019303_S1_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T019929_S13_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T019957_S2_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T020508_S3_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T021468_S4_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T021956_S5_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022010_S6_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022082_S14_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022088_S15_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022129_S7_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022146_S16_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022149_S17_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022151_S8_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022155_S9_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022190_S18_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022283_S10_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022378_S19_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022387_S11_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/TEM-TS-260521_S12_L001_R1_001.fastq.gz'], 'R2': ['/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T019303_S1_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T019929_S13_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T019957_S2_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T020508_S3_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T021468_S4_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T021956_S5_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022010_S6_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022082_S14_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022088_S15_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022129_S7_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022146_S16_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022149_S17_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022151_S8_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022155_S9_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022190_S18_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022283_S10_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022378_S19_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022387_S11_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/TEM-TS-260521_S12_L001_R2_001.fastq.gz'], 'analysis': {'cleanning_rule': {'R1_end_adapter': '/Anapath/anapath_resources/current/designs/Enrich_Solid-Tumor_V3/adapters/Illumina_3prim_adapter.fasta', 'R2_end_adapter': '/Anapath/anapath_resources/current/designs/Enrich_Solid-Tumor_V3/adapters/Illumina_5prim_adapter_rvc.fasta', 'adapter_error_rate': 0.1, 'adapter_min_overlap': 11}, 'depth_rule': {'expected_min_depth': 150}, 'evalPositiveCtrl_rule': {'error_threshold': 0.33, 'expected_variants': '/Anapath/anapath_resources/current/designs/Enrich_Solid-Tumor_V3/GRCh38/pos_ctrl_expected.vcf', 'samples': ['TEM-TS-260521_S12_L001']}, 'fastqc_rule': {'adapters': '/Anapath/anapath_resources/current/fastqc/adapter_list.txt', 'contaminants': '/Anapath/anapath_resources/current/fastqc/contaminant_list.txt', 'is_grouped': False}, 'filterVCF_rule': {'annotations_rules': '/Anapath/anapath_resources/current/designs/Enrich_Solid-Tumor_V3/filters_annot.json', 'homopolym_length': 5, 'kept_RNA': '/Anapath/anapath_resources/current/designs/Enrich_Solid-Tumor_V3/reference_RNA.tsv', 'kept_consequences': ['TFBS_ablation', 'TFBS_amplification', 'TF_binding_site_variant', 'regulatory_region_ablation', 'regulatory_region_amplification', 'transcript_ablation', 'splice_acceptor_variant', 'splice_donor_variant', 'stop_gained', 'frameshift_variant', 'stop_lost', 'start_lost', 'transcript_amplification', 'inframe_insertion', 'inframe_deletion', 'missense_variant', 'protein_altering_variant', 'splice_region_variant'], 'known_artifacts': '/Anapath/anapath_resources/current/designs/Enrich_Solid-Tumor_V3/GRCh38/variants_noise_MiSeq.tsv', 'low_alt_count': 10, 'low_alt_fraction': 0.02, 'low_calling_depth': 50, 'polymorphism_threshold': 0.01, 'variants_rules': '/Anapath/anapath_resources/current/designs/Enrich_Solid-Tumor_V3/filters_record.json'}, 'freebayes_rule': {'min_alt_count': 4, 'min_alt_fraction': 0.017, 'min_base_qual': 15}, 'hgvs_rule': {'mutalyzer_url': 'http://srvhpchgvs:9897/proxy', 'proxy_url': None}, 'mutect2_rule': {'min_alt_count': 4, 'min_alt_fraction': 0.017, 'min_base_qual': 15}, 'shallowsAnalysis_rule': {'depth_mode': 'fragment', 'expected_min_depth': 100}, 'vardict_rule': {'keep_multiple_alt': True, 'min_alt_count': 4, 'min_alt_fraction': 0.017, 'min_base_qual': 15}, 'vep_rule': {'dbNSFP_fields': ['MetaLR_rankscore', 'VEST4_rankscore'], 'vep_cache': '/Anapath/bank/Homo_sapiens/DNA/GRCh38_Ensembl101/vep'}}, 'disease': {'by_sample': {}, 'ontology': '/Anapath/bank/Homo_sapiens/ontologies/disease_ontology/HumanDO_2021-03-29.owl'}, 'interop': '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/InterOp', 'reference': {'accessions': '/Anapath/bank/Homo_sapiens/DNA/GRCh38_Ensembl101/sequences/assembly_accessions.tsv', 'annotations': {'genes': '/Anapath/bank/Homo_sapiens/DNA/GRCh38_Ensembl101/annotations/Homo_sapiens.GRCh38.ensembl_v101.chr.gtf.gz'}, 'assembly': 'GRCh38', 'clinical_evidences': '/Anapath/bank/Homo_sapiens/clinical_evidences/genovance_db_r1.tsv', 'known_variants': {'cosmic': '/Anapath/bank/Homo_sapiens/DNA/GRCh38_Ensembl101/variants/Cosmic_v92_CodingMuts_normal.vcf.gz', 'dbsnp': '/Anapath/bank/Homo_sapiens/DNA/GRCh38_Ensembl101/variants/dbSNP_v151.vcf.gz', 'gnomad': '/Anapath/bank/Homo_sapiens/DNA/GRCh38_Ensembl101/variants/gnomad.genomes.r3.0.sites.vcf.gz', 'mills_indels': '/Anapath/bank/Homo_sapiens/DNA/GRCh38_Ensembl101/variants/Mills_and_1000G_gold_standard.indels.hg38.vcf.gz'}, 'sequences': '/Anapath/bank/Homo_sapiens/DNA/GRCh38_Ensembl101/sequences/Homo_sapiens.GRCh38.ensembl_v101.dna.toplevel.chrOnly.fa', 'species': 'Homo sapiens', 'variants_pathogenicity': {'CADD': ['/Anapath/bank/Homo_sapiens/DNA/GRCh38_Ensembl101/pathogenicity/CADDv1.6_whole_genome_SNVs.tsv.gz', '/Anapath/bank/Homo_sapiens/DNA/GRCh38_Ensembl101/pathogenicity/CADDv1.6_gnomad.genomes.r3.0.indel.tsv.gz'], 'dbNSFP': '/Anapath/bank/Homo_sapiens/DNA/GRCh38_Ensembl101/pathogenicity/dbNSFP_v4.1a.gz'}}, 'software_pathes': {}, 'targets': '/Anapath/anapath_resources/current/designs/Enrich_Solid-Tumor_V3/GRCh38/targets.bed'}",
        "start_date": "2021-05-29 00:00:00",
        "end_date": "2021-05-30 00:00:00",
        "software_version": "1.2.0",
        "software": 36
        }"""

id_json: str = AnalysisAPI.createWS(data_json)
print(id_json, '\r\n')

"""
RUN_SAMPLE CREATING WS
"""
print('RUN_SAMPLE CREATING WS')

data_json = """{
        "run": 18,
        "sample": 324
        }"""

id_json: str = RunSampleAPI.createWS(data_json)
print(id_json, '\r\n')

"""
RESULT_CONSUMER CREATING WS
"""
print('RESULT_CONSUMER CREATING WS')

data_json = """{
        "consumer": 96,
        "result": 2808
        }"""

id_json: str = ResultConsumerAPI.createWS(data_json)
print(id_json, '\r\n')

"""
SAMPLE_RESULT CREATING WS
"""
print('SAMPLE_RESULT CREATING WS')

data_json = """{
        "result": 2808,
        "sample": 324
        }"""

id_json: str = ResultConsumerAPI.createWS(data_json)
print(id_json, '\r\n')

"""
SAMPLE PARENT UPDATING WS
"""
print('SAMPLE PARENT UPDATING WS')

id_json: str = SampleAPI.updateParentSampleWS(2, 1)
print(id_json, '\r\n')


"""
RESULT UPDATING WS
"""
print('RESULT UPDATING WS')

data_dict = {
        "category": "raw_reads",
        "path": "test path",
        "type": "fastq",
        "run": 18
        }

id_json: str = ResultAPI.updateResultWS(1, data_dict)
print(id_json, '\r\n')


"""
SAMPLE READING WS
"""
print('SAMPLE READING WS')

data_json: str = SampleAPI.readWS(1)
print(data_json, '\r\n')

"""
RUN READING WS
"""
print('RUN READING WS')

data_json: str = RunAPI.readWS(1)
print(data_json, '\r\n')

"""
RESULT READING WS
"""
print('RESULT READING WS')

data_json: str = ResultAPI.readWS(1)
print(data_json, '\r\n')

"""
ANALYSIS READING WS
"""
print('ANALYSIS READING WS')

data_json: str = AnalysisAPI.readWS(1)
print(data_json, '\r\n')

"""
SAMPLE ALL READING WS
"""
print('SAMPLE ALL READING WS')

data_json: str = SampleAPI.readWS()
print(data_json, '\r\n')

"""
RUN ALL READING WS
"""
print('RUN ALL READING WS')

data_json: str = RunAPI.readWS()
print(data_json, '\r\n')

"""
RESULT ALL READING WS
"""
print('RESULT ALL READING WS')

data_json: str = ResultAPI.readWS()
print(data_json, '\r\n')

"""
ANALYSIS ALL READING WS
"""
print('ANALYSIS ALL READING WS')

data_json: str = AnalysisAPI.readWS()
print(data_json, '\r\n')
```