"""
Functions for doing requests on variant database objects
"""

import json
import re
from typing import Optional, List

from variant.model_data.parentData import DataModel
from variant.model_data.repository.parentRepository import RepositoryModel
from variant.model_data.variant import Variant


class VariantRepository(RepositoryModel):
    """
    Requests on variants
    """

    @staticmethod
    def create(variant: Variant,
               collect: object = DataModel.get_collect()):
        """
        Data variant inserted on the database

        @param variant: Variant data
        @param collect: Collection of the database
        @return: The id of the variant saved
        @rtype: str
        """
        data_json = json.dumps(variant, default=lambda o: o.__dict__)
        data_dict = json.loads(data_json)
        req = collect.insert_one(data_dict)

        return str(req.inserted_id)

    @staticmethod
    def find_distinct_filters(sample_name: str,
                              collect: object = DataModel.get_collect()):
        """
        Find the distinct filters for the sample

        :param collect: Collection of the database
        :param sample_name: Name of the sample
        :return: Distinct filter list
        :rtype: [str]
        """
        req = collect.find({
            'sample_name': sample_name,
        }
        ).distinct('supports.filters')

        return list(req)

    @staticmethod
    def find_variants_frequency(sample_name: str,
                                frequency: float,
                                comparator: str,
                                collect: object = DataModel.get_collect()):
        """
        Return the list of variants according with the frequency indicated

        :param collect: Collection of the database
        :param sample_name: Name of the sample
        :param frequency: Value wanted
        :param comparator: Comparaison operator used for the find request
        :return: Json Variant list
        :rtype: [dict]
        """

        comparator = '$' + comparator
        req = collect.find({
            'sample_name': sample_name,
            'supports.frequency': {comparator: frequency}
        },
            {
                '_id': 0
            }
        )

        return list(req)

    @staticmethod
    def find_variants_node_value(sample_name: str,
                                 node: str,
                                 values: Optional[List['str']],
                                 collect: object = DataModel.get_collect(),
                                 ignore_case: bool = False):
        """
        Return the variant list for which the node contains the text searched

        :param collect: Collection of the database
        :param sample_name: Name of the sample
        :param node: Node of the json variant
        :param values: Values searched
        :param ignore_case: The case is ignored or not
        :return: The json variant list for which the node contains at least one of the searched texts
        :rtype: [dict]
        """
        reg = []
        for v in values:
            reg.append('^.*' + v)

        if ignore_case:
            regex = re.compile('|'.join(reg), re.IGNORECASE)
        else:
            regex = re.compile('|'.join(reg))

        req = collect.find({
            'sample_name': sample_name,
            node: regex
        },
            {
                '_id': 0
            }
        )

        return list(req)
