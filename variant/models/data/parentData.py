"""
:todo check the optional or not values
"""

from pymongo import MongoClient


class DataModel:
    """
    All the objects managed by the mongodb database inherit of DataModel
    """

    @classmethod
    def from_json(cls, data: dict) -> dict:
        """
        Return the data object according of the json data representation

        :param data: object dict
        :type data: dict
        :rtype: DataModel
        """
        return cls(**data)


    @staticmethod
    def get_collect() -> object:
        """
        Reach to the collection of the database

        :rtype: object
        """
        client = MongoClient()
        db = client.variant_project
        collect = db.variants

        return collect

