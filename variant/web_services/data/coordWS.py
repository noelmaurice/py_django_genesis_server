"""
Classes and functions for accessing to Coord, part of a variant
See similary data object documentation

The data access is realized thanks web services
"""

from typing import Optional

from variant.models.data.coord import Coord
from variant.web_services.data.parentWS import WSModel


class CoordWS(WSModel):
    """
    The coord part of a variant
    """
    alt: str
    assembly: Optional[str]
    pos: int
    ref: str
    region: str

    class Config:
        orm_mode = True

    def toData(self):
        data = Coord(self.alt, self.assembly, self.pos, self.ref, self.region)

        return data
