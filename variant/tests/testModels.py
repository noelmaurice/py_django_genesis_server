"""
Testing variant data with database
"""
import json

from variant.model_data.data.variant import Variant
from variant.model_data.repository.variantRepository import VariantRepository
from variant.tests.parentTest import ParentTest


class VariantDataTestClass(ParentTest):
    """
    Class for testing variant data with database
    """
    @classmethod
    def setUpTestData(cls):
        """
        Function called before all tests defined in the class
        """
        path_file = 'variant/tests/files/test_variants.json'
        ParentTest.get_test_collect().remove()

        with open(path_file, 'r') as data_file:
            data_json = data_file.read()

        data_dict = json.loads(data_json)
        for d in data_dict:
            VariantRepository.create(d, ParentTest.get_test_collect())


    def setUp(self):
        """
        Function called before each test defined in the class
        """
        pass

    def test_three_variants_inserted(self):
        """
        The insertion of the variants in the database is checked
        """
        req = ParentTest.get_test_collect().find({}).count()

        self.assertEqual(req, 3)

    def test_find_distinct_filters(self):
        """
        The request for finding filters for a sample is checked
        """
        filters = VariantRepository.find_distinct_filters('splTOTO',
                                                          collect=ParentTest.get_test_collect())

        self.assertEqual(['CSQ', 'OOT', 'PASS', 'q10'], list(filters))

    def test_find_variant_frequencies(self):
        """
        The request for finding sample with a some frequency is checked
        """

        variants = VariantRepository.find_variants_frequency('splTOTO', 40.00,
                                                             operator='lt',
                                                             collect=ParentTest.get_test_collect())

        self.assertEqual(1, len(variants))

    def test_find_node_contains_value(self):
        """
        The request for finding sample with some value for a specific node is checked
        """
        variants = VariantRepository.find_variants_node_value('splTOTO',
                                                            'annot.changes.HGVSc', ['524G>A'],
                                                              collect=ParentTest.get_test_collect())

        self.assertEqual(1, len(variants))

    def test_deserialization(self):
        """
        Test the variant dict to variant object
        """
        data_dict = ParentTest.get_test_collect().find({}).limit(1)
        data_obj = Variant.from_json(data_dict[0])

        self.assertEqual('NM_000314.8', data_obj.annot[0].subject['feature'])
        self.assertEqual('A', data_obj.coord['alt'])
        self.assertEqual('splice_donor_variant', data_obj.annot[0].conseq)
