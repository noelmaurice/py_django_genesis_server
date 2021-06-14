"""
Classes and functions for accessing to Supports, part of a variant
See similary data object documentation

The data access is realized thanks web services
"""
from typing import Optional, List

from variant.models.data.supports import Support
from variant.web_services.data.parentWS import WSModel


class SupportWS(WSModel):
    """
    The Support for a variant
    """

    filters: Optional[List[str]]
    alt_depth: Optional[int]
    depth: Optional[int]
    frequency: Optional[float]
    quality: Optional[float]
    source: Optional[str]

    class Config:
        orm_mode = True

    def toData(self) -> Support:
        data = Support(self.filters, self.alt_depth, self.depth, self.frequency, self.quality, self.source)

        return data

