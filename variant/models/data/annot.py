"""
Classes and functions for managing a annotation, part of a variant
"""

import anacore.vcf

from variant.models.data.parentData import DataModel


class Changes(DataModel):
    """
    Changes object, part of a annot or collocated
    This object can be managed by the database
    """

    def __init__(self,
                 HGVSc: str,
                 HGVSp: str) -> None:
        """
        :param HGVSc: HGVSc for the changes part of the annot
        :param HGVSp: HGVSp for the changes part of the annot
        """
        self.HGVSc = HGVSc
        self.HGVSp = HGVSp


class Pathogenicity(DataModel):
    """
    Pathogenicity object, part of a annot or collocated
    This object can be managed by the database
    """

    def __init__(self,
                 CADD_phred: str,
                 ClinVar: str,
                 MetaLR_rankscore: str,
                 VEST4_rankscore: str):
        """
        :param CADD_phred: CADD_phred of the pathogenicity part of the annot
        :param ClinVar: ClinVar of the pathogenicity part of the annot
        :param MetaLR_rankscore: MetaLR_rankscore of the pathogenicity part of the annot
        :param VEST4_rankscore: VEST4_rankscore of the pathogenicity part of the annot
        """
        self.CADD_phred = CADD_phred
        self.ClinVar = ClinVar
        self.MetaLR_rankscore = MetaLR_rankscore
        self.VEST4_rankscore = VEST4_rankscore


class Subject(DataModel):
    """
    Subject object, part of a annot or collocated
    This object can be managed by the database
    """

    def __init__(self,
                 feature: str,
                 feature_type: str,
                 symbol: str):
        """

        :param feature:
        :param feature_type:
        :param symbol:
        """
        self.feature = feature
        self.feature_type = feature_type
        self.symbol = symbol


class Annot(DataModel):
    """
    The annot or the collocated annot, part of a variant
    This object can be managed by the database
    """

    def __init__(self,
                 conseq: str,
                 changes: Changes,
                 pathogenicity: Pathogenicity,
                 subject: Subject):
        """
        :param conseq: conseq part of the annot
        :param changes: chances part of the annot
        :param pathogenicity: pathogenicity part of the annot
        :param subject: subject part of the annot
        """
        self.conseq = conseq
        self.changes = changes
        self.pathogenicity = pathogenicity
        self.subject = subject


    @classmethod
    def create_all(cls, record: anacore.vcf.VCFRecord, info_ann: [str]):
        """
        All the annot and collocated_annot of the variant are created

        :param record: Record containing the variant information and for one sample
        :param info_ann: Annotations about the variant
        :return: The annot list and collocated_annot list
        :rtype: [[Annot], [Annot]]
        """

        try:
            alt = record.alt[0]

            annots = []
            collocated_annots = []
            for info_a in info_ann:
                info_a_allele = info_a['Allele']

                changes = Changes(info_a['HGVSc'], info_a['HGVSp'])
                pathogenicity = Pathogenicity(info_a['CADD_PHRED'], info_a['CLIN_SIG'], info_a['MetaLR_rankscore'],
                                              info_a['VEST4_rankscore'])
                subject = Subject(info_a['Feature'], info_a['Feature_type'], info_a['SYMBOL'])
                a = Annot(info_a['Consequence'], changes, pathogenicity, subject)

                if (info_a_allele == alt):
                    annots.append(a)
                else:
                    collocated_annots.append(a)
        except Exception:
            raise Exception('Error while Annot creation')

        return annots, collocated_annots


