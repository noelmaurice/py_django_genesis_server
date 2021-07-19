from django.test import TestCase
from pymongo import MongoClient


class ParentTest(TestCase):
    """
    All the test objects managed by the mongodb test database inherit of DataTestModel
    """

    pass

    @staticmethod
    def get_test_collect():
        """
        Access to the test collection of the database

        :rtype: object
        """
        client = MongoClient()
        db = client.genesis
        collect = db.test_variant

        return collect
