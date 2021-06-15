"""
Classes and functions for accessing to annotation, part of a variant
See similary data object documentation

The variant data access can be realized thanks the web services
"""

from typing import Optional

from variant.models.data.annot import Changes, Pathogenicity, Subject, Annot
from variant.web_services.data.parentWS import WSModel


class ChangesWS(WSModel):
    """
    Changes object, part of a annot or collocated web service object
    """

    HGVSc: Optional[str]
    HGVSp: Optional[str]

    class Config:
        orm_mode = True

    def toData(self) -> Changes:
        data = Changes(self.HGVSc, self.HGVSp)

        return data


class PathogenicityWS(WSModel):
    """
    Pathogenicity object, part of a annot or collocated web service object
    """

    CADD_phred: Optional[str]
    ClinVar: Optional[str]
    MetaLR_rankscore: Optional[str]
    VEST4_rankscore: Optional[str]

    class Config:
        orm_mode = True

    def toData(self) -> Pathogenicity:
        data = Pathogenicity(self.CADD_phred, self.ClinVar, self.MetaLR_rankscore, self.VEST4_rankscore)

        return data

class SubjectWS(WSModel):
    """
    Subject object, part of a annot or collocated web service object
    """

    feature: Optional[str]
    feature_type: Optional[str]
    symbol: Optional[str]

    class Config:
        orm_mode = True

    def toData(self) -> Subject:
        data = Subject(self.feature, self.feature_type, self.symbol)

        return data


class AnnotWS(WSModel):
    """
    The annot or the collocated annot, part of a variant web service object
    """

    conseq: Optional[str]
    changes: ChangesWS
    pathogenicity: PathogenicityWS
    subject: SubjectWS

    class Config:
        orm_mode = True

    def toData(self) -> Annot:
        annot = Annot(self.conseq,
                      self.changes.toData(),
                      self.pathogenicity.toData(),
                      self.subject.toData())

        return annot
