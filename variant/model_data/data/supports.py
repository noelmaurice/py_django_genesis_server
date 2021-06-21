"""
Classes and functions for managing a Supports, part of a variant
"""

import anacore.vcf

from variant.model_data.data.parentData import DataModel


class Support(DataModel):
    """
    The Support for a variant
    This object can be managed by the database
    """
    def __init__(self,
                 filters: [str],
                 alt_depth: int,
                 depth: int,
                 frequency: float,
                 quality: float,
                 source: str) -> None:
        """
        :param filters: Filters of the variant
        :param alt_depth: Alternative depth
        :param depth: Reference depth
        :param frequency: Alternative depth compared to reference depth, calculated field
        :param quality: Quality
        :param source: Source
        """
        self.filters = filters
        self.alt_depth = alt_depth
        self.depth = depth
        self.frequency = frequency
        self.quality = quality
        self.source = source

    @classmethod
    def create_all(cls, record: anacore.vcf.VCFRecord, sample: tuple) -> [DataModel]:
        """
        All the Support of the variant supports part are created

        :param record: Record containing the variant information and for one sample
        :param sample: Sample of the variant
        :return: The Support list for the supports part of the variant
        :rtype: [Support]
        """
        try:
            supports = []

            filters = record.filter

            ADs = sample[1]['ADSRC']
            DPs = sample[1]['DPSRC']
            SRCs = record.info['SRC']

            QUALs = []
            for i in range(len(ADs)):
                vc_qual_name = 's' + str(i) + '_VCQUAL'
                value = None
                try:
                    value = record.info[vc_qual_name]
                except Exception:
                    value = None
                finally:
                    QUALs.append(value)

            for i in range(len(ADs)):
                alt_depth = ADs[i]
                depth = DPs[i]

                if (depth != 0):
                    frequency = round((alt_depth / depth) * 100, 2)
                else:
                    frequency = None

                support = Support(filters, alt_depth, depth, frequency, QUALs[i], SRCs[i])
                supports.append(support)

        except Exception:
            raise Exception('Error while Supports creation')

        return supports