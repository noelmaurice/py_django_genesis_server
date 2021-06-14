"""
Classes and functions for accessing to Xref, part of a variant
See data object :func:'variant.models.vcf.data.xref'
"""
from typing import Optional, List

from variant.models.data.xref import Xref
from variant.web_services.data.parentWS import WSModel


class XrefWS(WSModel):
    """
    The xref part of a variant
    """

    HGMD: Optional[List['str']]
    Unknown: Optional[List['str']]
    cosmic: Optional[List['str']]
    dbSNP: Optional[List['str']]

    class Config:
        orm_mode = True

    def toData(self) -> Xref:
        data = Xref(self.HGMD, self.Unknown, self.cosmic, self.dbSNP)

        return data


