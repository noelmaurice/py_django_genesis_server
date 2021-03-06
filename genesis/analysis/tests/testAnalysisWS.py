"""
@TODO The web services must be called in test mode
@TODO The test database data must be initialed before tests
"""

"""
Testing variant data with database
"""

from rest_framework import status

from genesis.analysis.tests.parentTest import ParentTest


class VariantWebServiceTestClass(ParentTest):
    """
    Class for testing the web services.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Function called before all tests defined in the class
        """

    def setUp(self):
        """
        Function called before each test defined in the class
        """
        pass

    def test_read_sample_result_status_200(self):

        # get sample test
        url = 'http://{host}:{port}/ws/analysis/sample/1/'
        response = ParentTest.requestWS(url, method='get')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_read_all_sample_result_status_200(self):

        # get all sample test
        url = 'http://{host}:{port}/ws/analysis/sample/'
        response = ParentTest.requestWS(url, method='get')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_read_result_result_status_200(self):

        # get result test
        url = 'http://{host}:{port}/ws/analysis/result/1/'
        response = ParentTest.requestWS(url, method='get')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_read_all_result_result_status_200(self):

        # get all result test
        url = 'http://{host}:{port}/ws/analysis/result/'
        response = ParentTest.requestWS(url, method='get')
        self.assertEqual(status.HTTP_200_OK, response.status_code)


    def test_read_run_result_status_200(self):

        # get run test
        url = 'http://{host}:{port}/ws/analysis/run/1/'
        response = ParentTest.requestWS(url, method='get')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_read_all_run_result_status_200(self):

        # get all run test
        url = 'http://{host}:{port}/ws/analysis/run/'
        response = ParentTest.requestWS(url, method='get')
        self.assertEqual(status.HTTP_200_OK, response.status_code)


    def test_read_analysis_result_status_200(self):

        # get analysis test
        url = 'http://{host}:{port}/ws/analysis/analysis/1/'
        response = ParentTest.requestWS(url, method='get')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_read_all_analysis_result_status_200(self):
        # get all analysis test
        url = 'http://{host}:{port}/ws/analysis/analysis/1/'
        response = ParentTest.requestWS(url, method='get')
        self.assertEqual(status.HTTP_200_OK, response.status_code)


    def test_create_sample_status_201(self):
        """
        The web service for the sample insertion into the database is checked
        """
        data_json = """
            {
                "name": "splTOTO",
                "creation_date": "2021-07-26 00:00:00",
                "description": "Example of sample"
            }
            """

        url = 'http://{host}:{port}/ws/analysis/sample/'

        response = ParentTest.requestWS(url, data_json)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_update_sample_parent_status_200_400(self):
        """
        The web service for the sample update into the database is checked
        """

        url = 'http://{host}:{port}/ws/analysis/sample/2/parent/'

        data_json = """
            {
                "parent": 1
            }
            """

        response = ParentTest.requestWS(url, data_json, method='put')

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        url = 'http://{host}:{port}/ws/analysis/sample/-1/parent/'

        data_json = """
            {
                "parent": 2
            }
            """
        response = ParentTest.requestWS(url, data_json, method='put')

        self.assertNotEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

        url = 'http://{host}:{port}/ws/analysis/sample/1/parent/'

        data_json = """
                    {
                        "parent": 2
                    }
                    """
        response = ParentTest.requestWS(url, data_json, method='put')

        self.assertNotEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_create_sample_tag_status_201(self):
        """
        The web service for the sample_tag data insertion into the database is checked
        """
        data_json = """
            {
                "key": "origin",
                "value": "anapath",
                "type": "str",
                "sample": 324
            }
            """

        url = 'http://{host}:{port}/ws/analysis/sample_tag/'

        response = ParentTest.requestWS(url, data_json)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)


    def test_create_run_status_201(self):
        """
        The web service for the run data insertion into the database is checked
        """
        data_json = """
            {
                "start_date": "2021-05-29 00:00:00",
                "end_date": "2021-05-30 00:00:00",
                "instrument": 18
            }
            """

        url = 'http://{host}:{port}/ws/analysis/run/'

        response = ParentTest.requestWS(url, data_json)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)


    def test_create_software_status_201(self):
        """
        The web service for the software data insertion into the database is checked
        """
        data_json = """
            {
                "category": "conversion",
                "description": "Conversion Software both demultiplexes data and converts BCL files generated by Illumina sequencing systems to standard FASTQ file formats for downstream analysis.",
                "name": "bcl2fastq"
            }
            """

        url = 'http://{host}:{port}/ws/analysis/software/'

        response = ParentTest.requestWS(url, data_json)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)


    def test_create_analysis_status_201(self):
        """
        The web service for the analysis data insertion into the database is checked
        """
        data_json = """
            {
                "cmd": "{'R1': ['/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T019303_S1_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T019929_S13_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T019957_S2_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T020508_S3_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T021468_S4_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T021956_S5_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022010_S6_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022082_S14_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022088_S15_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022129_S7_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022146_S16_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022149_S17_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022151_S8_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022155_S9_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022190_S18_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022283_S10_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022378_S19_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022387_S11_L001_R1_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/TEM-TS-260521_S12_L001_R1_001.fastq.gz'], 'R2': ['/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T019303_S1_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T019929_S13_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T019957_S2_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T020508_S3_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T021468_S4_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T021956_S5_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022010_S6_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022082_S14_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022088_S15_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022129_S7_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022146_S16_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022149_S17_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022151_S8_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022155_S9_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022190_S18_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022283_S10_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022378_S19_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T022387_S11_L001_R2_001.fastq.gz', '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/TEM-TS-260521_S12_L001_R2_001.fastq.gz'], 'analysis': {'cleanning_rule': {'R1_end_adapter': '/Anapath/anapath_resources/current/designs/Enrich_Solid-Tumor_V3/adapters/Illumina_3prim_adapter.fasta', 'R2_end_adapter': '/Anapath/anapath_resources/current/designs/Enrich_Solid-Tumor_V3/adapters/Illumina_5prim_adapter_rvc.fasta', 'adapter_error_rate': 0.1, 'adapter_min_overlap': 11}, 'depth_rule': {'expected_min_depth': 150}, 'evalPositiveCtrl_rule': {'error_threshold': 0.33, 'expected_variants': '/Anapath/anapath_resources/current/designs/Enrich_Solid-Tumor_V3/GRCh38/pos_ctrl_expected.vcf', 'samples': ['TEM-TS-260521_S12_L001']}, 'fastqc_rule': {'adapters': '/Anapath/anapath_resources/current/fastqc/adapter_list.txt', 'contaminants': '/Anapath/anapath_resources/current/fastqc/contaminant_list.txt', 'is_grouped': False}, 'filterVCF_rule': {'annotations_rules': '/Anapath/anapath_resources/current/designs/Enrich_Solid-Tumor_V3/filters_annot.json', 'homopolym_length': 5, 'kept_RNA': '/Anapath/anapath_resources/current/designs/Enrich_Solid-Tumor_V3/reference_RNA.tsv', 'kept_consequences': ['TFBS_ablation', 'TFBS_amplification', 'TF_binding_site_variant', 'regulatory_region_ablation', 'regulatory_region_amplification', 'transcript_ablation', 'splice_acceptor_variant', 'splice_donor_variant', 'stop_gained', 'frameshift_variant', 'stop_lost', 'start_lost', 'transcript_amplification', 'inframe_insertion', 'inframe_deletion', 'missense_variant', 'protein_altering_variant', 'splice_region_variant'], 'known_artifacts': '/Anapath/anapath_resources/current/designs/Enrich_Solid-Tumor_V3/GRCh38/variants_noise_MiSeq.tsv', 'low_alt_count': 10, 'low_alt_fraction': 0.02, 'low_calling_depth': 50, 'polymorphism_threshold': 0.01, 'variants_rules': '/Anapath/anapath_resources/current/designs/Enrich_Solid-Tumor_V3/filters_record.json'}, 'freebayes_rule': {'min_alt_count': 4, 'min_alt_fraction': 0.017, 'min_base_qual': 15}, 'hgvs_rule': {'mutalyzer_url': 'http://srvhpchgvs:9897/proxy', 'proxy_url': None}, 'mutect2_rule': {'min_alt_count': 4, 'min_alt_fraction': 0.017, 'min_base_qual': 15}, 'shallowsAnalysis_rule': {'depth_mode': 'fragment', 'expected_min_depth': 100}, 'vardict_rule': {'keep_multiple_alt': True, 'min_alt_count': 4, 'min_alt_fraction': 0.017, 'min_base_qual': 15}, 'vep_rule': {'dbNSFP_fields': ['MetaLR_rankscore', 'VEST4_rankscore'], 'vep_cache': '/Anapath/bank/Homo_sapiens/DNA/GRCh38_Ensembl101/vep'}}, 'disease': {'by_sample': {}, 'ontology': '/Anapath/bank/Homo_sapiens/ontologies/disease_ontology/HumanDO_2021-03-29.owl'}, 'interop': '/MiSeqDx1/210529_M70265_0465_000000000-JHLN6/InterOp', 'reference': {'accessions': '/Anapath/bank/Homo_sapiens/DNA/GRCh38_Ensembl101/sequences/assembly_accessions.tsv', 'annotations': {'genes': '/Anapath/bank/Homo_sapiens/DNA/GRCh38_Ensembl101/annotations/Homo_sapiens.GRCh38.ensembl_v101.chr.gtf.gz'}, 'assembly': 'GRCh38', 'clinical_evidences': '/Anapath/bank/Homo_sapiens/clinical_evidences/genovance_db_r1.tsv', 'known_variants': {'cosmic': '/Anapath/bank/Homo_sapiens/DNA/GRCh38_Ensembl101/variants/Cosmic_v92_CodingMuts_normal.vcf.gz', 'dbsnp': '/Anapath/bank/Homo_sapiens/DNA/GRCh38_Ensembl101/variants/dbSNP_v151.vcf.gz', 'gnomad': '/Anapath/bank/Homo_sapiens/DNA/GRCh38_Ensembl101/variants/gnomad.genomes.r3.0.sites.vcf.gz', 'mills_indels': '/Anapath/bank/Homo_sapiens/DNA/GRCh38_Ensembl101/variants/Mills_and_1000G_gold_standard.indels.hg38.vcf.gz'}, 'sequences': '/Anapath/bank/Homo_sapiens/DNA/GRCh38_Ensembl101/sequences/Homo_sapiens.GRCh38.ensembl_v101.dna.toplevel.chrOnly.fa', 'species': 'Homo sapiens', 'variants_pathogenicity': {'CADD': ['/Anapath/bank/Homo_sapiens/DNA/GRCh38_Ensembl101/pathogenicity/CADDv1.6_whole_genome_SNVs.tsv.gz', '/Anapath/bank/Homo_sapiens/DNA/GRCh38_Ensembl101/pathogenicity/CADDv1.6_gnomad.genomes.r3.0.indel.tsv.gz'], 'dbNSFP': '/Anapath/bank/Homo_sapiens/DNA/GRCh38_Ensembl101/pathogenicity/dbNSFP_v4.1a.gz'}}, 'software_pathes': {}, 'targets': '/Anapath/anapath_resources/current/designs/Enrich_Solid-Tumor_V3/GRCh38/targets.bed'}",
                "start_date": "2021-05-29 00:00:00",
                "end_date": "2021-05-30 00:00:00",
                "software_version": "1.2.0",
                "software": 36
            }
            """

        url = 'http://{host}:{port}/ws/analysis/analysis/'

        response = ParentTest.requestWS(url, data_json)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)


    def test_create_provider_status_201(self):
        """
        The web service for the provider data insertion into the database is checked
        """
        data_json = """
            {
                "description": "Illumina, Inc. is an American company incorporated in April 1998 that develops, manufactures and markets integrated systems for the analysis of genetic variation and biological function.",
                "name": "Illumina"
            }
            """

        url = 'http://{host}:{port}/ws/analysis/provider/'

        response = ParentTest.requestWS(url, data_json)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)


    def test_create_instrument_status_201(self):
        """
        The web service for the instrument data insertion into the database is checked
        """
        data_json = """
            {
                "model": "MiSeq",
                "provider_sn": "M70265",
                "category": "High-throughput sequencer",
                "provider": 19
            }
            """

        url = 'http://{host}:{port}/ws/analysis/instrument/'

        response = ParentTest.requestWS(url, data_json)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)


    def test_create_result_status_201(self):
        """
        The web service for the result data insertion into the database is checked
        """
        data_json = """
            {
                "category": "raw_reads",
                "path": "/home/toto/share/data/raw/210529_M70265_0465_000000000-JHLN6/Data/Intensities/BaseCalls/21T019303_S1_L001_R1_001.fastq.gz",
                "type": "fastq",
                "run": 18
            }
            """

        url = 'http://{host}:{port}/ws/analysis/result/'

        response = ParentTest.requestWS(url, data_json)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)


    def test_update_result_status_200(self):
        """
        The web service for the result data insertion into the database is checked
        """
        data_json = """
            {
                "category": "raw_reads",
                "path": "21T019303_S1_L001_R1_001.fastq.gz",
                "type": "fastq",
                "run": 18
            }
            """

        url = 'http://{host}:{port}/ws/analysis/result/1/'

        response = ParentTest.requestWS(url, data_json, method='put')

        self.assertEqual(status.HTTP_200_OK, response.status_code)


    def test_create_run_tag_status_201(self):
        """
        The web service for the run_tag data insertion into the database is checked
        """
        data_json = """
            {
                "key": "flowcell_id",
                "value": "000000000-JHLN6",
                "type": "str",
                "run": 18
            }
                    """

        url = 'http://{host}:{port}/ws/analysis/run_tag/'

        response = ParentTest.requestWS(url, data_json)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_create_result_consumer_status_201(self):
        """
        The web service for the result_consumer data insertion into the database is checked
        """
        data_json = """
            {
                "consumer": 96,
                "result": 2808
            }
            """

        url = 'http://{host}:{port}/ws/analysis/result_consumer/'

        response = ParentTest.requestWS(url, data_json)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)


    def test_create_run_sample_status_201(self):
        """
        The web service for the run_sample data insertion into the database is checked
        """
        data_json = """
            {
                "run": 18,
                "sample": 324
            }
            """

        url = 'http://{host}:{port}/ws/analysis/run_sample/'

        response = ParentTest.requestWS(url, data_json)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)


    def test_create_sample_result_status_201(self):
        """
        The web service for the sample_result data insertion into the database is checked
        """
        data_json = """
            {
                "result": 2808,
                "sample": 324
            }
            """

        url = 'http://{host}:{port}/ws/analysis/sample_result/'

        response = ParentTest.requestWS(url, data_json)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)