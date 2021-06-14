"""
:todo check the optional or not values
"""
import this

from pymongo import MongoClient


class DataModel:
    """
    All the objects managed by the mongodb database inherit of DataModel
    """

    @classmethod
    def from_json(cls, data: dict) -> this:
        """
        Return the object according of the json data representation

        :param data: object dict
        :type data: dict
        :rtype: DataModel
        """
        return cls(**data)


    @staticmethod
    def get_collect() -> object:
        """
        Access to the collection of the database
        :rtype: object
        """
        client = MongoClient()
        db = client.variant_project
        collect = db.variants

        return collect

