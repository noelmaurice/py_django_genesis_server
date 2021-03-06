"""
Classes and functions for managing a Variant
"""

import anacore.vcf

from genesis.variant.model_data.annotData import Annot
from genesis.variant.model_data.coordData import Coord
from genesis.variant.model_data.evidencesData import Evidences
from genesis.variant.model_data.parentData import DataModel
from genesis.variant.model_data.popAFData import AlleleFrequency
from genesis.variant.model_data.supportsData import Support
from genesis.variant.model_data.xrefData import Xref


class Variant(DataModel):
    """
    Variant object
    This object can be managed by the database
    """

    def __init__(self,
                 sample_name: str,
                 annot: [Annot],
                 collated_annot: [Annot],
                 coord: Coord,
                 evidences: Evidences,
                 pop_AF: [AlleleFrequency],
                 supports: [Support],
                 xref: Xref) -> None:
        """
        :param sample_name: Sample name for the variant
        :param annot: annot part of the variant
        :param collated_annot: collocated part of the variant
        :param coord: coord part of the variant
        :param evidences: evidences part of the variant
        :param pop_AF: pop_AF part of the variant
        :param supports: supports part of the variant
        :param xref: xref part of the variant
        """
        self.sample_name = sample_name
        self.annot = annot
        self.collocated_annot = collated_annot
        self.coord = coord
        self.evidences = evidences
        self.pop_AF = pop_AF
        self.supports = supports
        self.xref = xref

    @classmethod
    def from_json(cls, data: dict):
        """
        Return the object according of the json data representation

        :param data: object dict
        :rtype: Variant
        """
        annot: [Annot] = list(map(Annot.from_json, data['annot']))
        collocated_annot: [Annot] = list(map(Annot.from_json, data["collocated_annot"]))
        supports: [Support] = list(map(Support.from_json, data["supports"]))
        pop_AF: [AlleleFrequency] = list(map(AlleleFrequency.from_json, data["pop_AF"]))
        return cls(data['sample_name'],
                   annot,
                   collocated_annot,
                   data['coord'],
                   data['evidences'],
                   pop_AF,
                   supports,
                   data['xref']
                   )

    @classmethod
    def create(cls,
               record: anacore.vcf.VCFRecord,
               sample: tuple,
               annotation: str = 'ANN',
               assembly: str = None):
        """
        The variant is created

        :param record: Record containing the variant information and for one sample
        :param sample: The sample considering for the variant
        :param annotation: The annotation part of the variant
        :param assembly: Assembly name
        :return: The variant object
        :rtype: Variant
        """
        variant: Variant

        try:
            info_ann = record.info[annotation]
        except:
            info_ann = None

        try:
            # annot
            annot, collocated_annot = Annot.create_all(record, info_ann)

            # coord
            coord = Coord.create(record, assembly)

            # evidences
            evidences = Evidences.create(sample)

            # pop AF
            AFs = AlleleFrequency.create_all(info_ann)

            # supports
            supports = Support.create_all(record, sample)

            # xref
            xref = Xref.create(info_ann)

            # variant
            variant = Variant(sample[0],
                              annot,
                              collocated_annot,
                              coord,
                              evidences,
                              AFs,
                              supports,
                              xref)

        except Exception:
            raise Exception('Error while Variant creation')

        return variant
