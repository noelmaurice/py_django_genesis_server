
"""
Classes and functions for accessing Variant thanks the web services
See similary data object documentation
"""
from typing import List, Optional

from variant.model_data.data.variant import Variant
from variant.web_services.data.annotWS import AnnotWS
from variant.web_services.data.coordWS import CoordWS
from variant.web_services.data.evidencesWS import EvidencesWS
from variant.web_services.data.parentWS import WSModel
from variant.web_services.data.popAFWS import AFWS
from variant.web_services.data.supportsWS import SupportWS
from variant.web_services.data.xrefWS import XrefWS


class VariantWS(WSModel):
    """
    Variant web service object
    """

    sample_name: str
    annot: Optional[List['AnnotWS']]
    collocated_annot: Optional[List['AnnotWS']]
    coord: CoordWS
    evidences: EvidencesWS
    pop_AF: Optional[List['AFWS']]
    supports: Optional[List['SupportWS']]
    xref: XrefWS

    class Config:
        orm_mode = True

    def toData(self):

        data = Variant(self.sample_name,
                       [annot.toData() for annot in self.annot],
                       [annot.toData() for annot in self.collocated_annot],
                       self.coord.toData(),
                       self.evidences.toData(),
                       [pop_AF.toData() for pop_AF in self.pop_AF],
                       [supports.toData() for supports in self.supports],
                       self.xref.toData())

        return data





