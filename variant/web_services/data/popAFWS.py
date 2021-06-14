"""
Classes and functions for accessing to popAF, part of a variant
See similary data object documentation

The data access is realized thanks web services
"""
from typing import Optional

from variant.models.data.popAF import AlleleFrequency
from variant.web_services.data.parentWS import WSModel


class AFWS(WSModel):
    """
    A AF of popAF, part of a variant
    """

    AF: Optional[float]
    name: Optional[str]
    source: Optional[str]

    class Config:
        orm_mode = True

    def toData(self) -> AF:
        data = AlleleFrequency(self.AF, self.name, self.source)

        return data
