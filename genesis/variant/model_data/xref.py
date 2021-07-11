"""
Classes and functions for managing a Xref, part of a variant
"""

from genesis.variant.model_data.parentData import DataModel

class Xref(DataModel):
    """
    The xref part of a variant
    This object can be managed by the database
    """

    def __init__(self,
                 HGMD: [str],
                 Unknown: [str],
                 cosmic: [str],
                 dbSNP: [str]) -> None:
        self.HGMD = HGMD
        self.Unknown = Unknown
        self.cosmic = cosmic
        self.dbSNP = dbSNP

    @classmethod
    def create(cls, info_ann: [str]) -> DataModel:
        """
        xref part is created for the variant

        :param info_ann: Annotations about the variant
        :return: The xref part of the variant
        :rtype: Xref
        """
        try:

            HGMD = []
            Unknown = []
            cosmic = []
            dbSNP = []

            for info_a in info_ann:
                existing_variation = info_a['Existing_variation']

                variations = existing_variation.split('&')
                for v in variations:
                    if v.startswith('CM'):
                        HGMD.append(v)
                    elif v.startswith('COS'):
                        cosmic.append(v)
                    elif v.startswith('rs'):
                        dbSNP.append(v)
                    else:
                        Unknown.append(v)

            HGMD = list(set(HGMD))
            Unknown = list(set(Unknown))
            cosmic = list(set(cosmic))
            dbSNP = list(set(dbSNP))

            xref = Xref(HGMD, Unknown, cosmic, dbSNP)

        except Exception:
            raise Exception('Error while Xref creation')

        return xref
