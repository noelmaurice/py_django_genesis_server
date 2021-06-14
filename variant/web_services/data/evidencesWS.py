"""
Classes and functions for accessing to Evidences, part of a variant
See data object :func:'variant.models.vcf.data.evidences'
"""
from typing import Optional

from variant.models.data.evidences import Evidences
from variant.web_services.data.parentWS import WSModel


class EvidencesWS(WSModel):
    """
    The evidences part of a variant
    """
    prec_same_dis: Optional[str]
    prec_all_dis: Optional[str]
    imp_same_dis: Optional[str]
    imp_all_dis: Optional[str]

    class Config:
        orm_mode = True

    def toData(self) -> Evidences:
        data = Evidences(self.prec_same_dis, self.prec_all_dis, self.imp_same_dis, self.imp_all_dis)

        return data
