"""
Classes and functions for managing a Evidences, part of a variant
"""

from variant.models.data.parentData import DataModel


class Evidences(DataModel):
    """
    The evidences part of a variant
    This object can be managed by the database
    """

    def __init__(self,
                 prec_same_dis: str,
                 prec_all_dis: str,
                 imp_same_dis: str,
                 imp_all_dis: str) -> None:
        """

        :param prec_same_dis: prec_same_dis for the variant
        :param prec_all_dis: prec_all_dis for the variant
        :param imp_same_dis: imp_same_dis for the variant
        :param imp_all_dis: imp_all_dis for the variant
        """
        self.prec_same_dis = prec_same_dis
        self.prec_all_dis = prec_all_dis
        self.imp_same_dis = imp_same_dis
        self.imp_all_dis = imp_all_dis

    @classmethod
    def create(cls, sample: tuple) -> DataModel:
        """
        evidences part is created for the variant

        :param sample: Sample of the variant
        :return: The Evidences object
        :rtype: Evidences
        """
        try:
            evidences = Evidences(
                sample[1]['EVID_PS'],
                sample[1]['EVID_IS'],
                sample[1]['EVID_IA'],
                sample[1]['EVID_PA'])

        except Exception:
            raise Exception('Error while Evidences creation')

        return evidences
