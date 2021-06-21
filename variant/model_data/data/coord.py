"""
Classes and functions for managing a Coord, part of a variant
"""
import anacore.vcf

from variant.model_data.data.parentData import DataModel


class Coord(DataModel):
    """
    The coord part of a variant
    This object can be managed by the database
    """
    def __init__(self,
                 alt: str,
                 assembly: str,
                 pos: int,
                 ref: str,
                 region: str) -> None:
        """

        :param alt: alt of the variant
        :param assembly:  assembly for the variant
        :param pos: pos of the variant
        :param ref: ref of the variant
        :param region: region of the variant
        """
        self.alt = alt
        self.assembly = assembly
        self.pos = pos
        self.ref = ref
        self.region = region

    @classmethod
    def create(cls, record: anacore.vcf.VCFRecord, assembly: str) -> DataModel:
        """
        Coord part is created for the variant

        :param record: Record containing the variant information and for one sample
        :param assembly: Assembly name
        :return: The coord object
        :rtype: Coord
        """
        try:
            pos = record.pos
            ref = record.ref
            chrom = record.chrom

            alt = record.alt
            if alt != None and len(alt) == 1:
                alt = alt[0]

            coord = Coord(alt, assembly, pos, ref, chrom)


        except Exception:
            raise Exception('Error while Coord creation')

        return coord