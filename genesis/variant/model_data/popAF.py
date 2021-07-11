"""
Classes and functions for managing a popAF, part of a variant
"""

from genesis.variant.model_data.parentData import DataModel


class AlleleFrequency(DataModel):
    """
    A AF of popAF, part of a variant
    This object can be managed by the database
    """

    def __init__(self,
                 AF: float,
                 name: str,
                 source: str) -> None:
        """
        :param AF: AF value
        :param name: AF name
        :param source: Source of AF
        """
        self.AF = AF
        self.name = name
        self.source = source

    @classmethod
    def create_all(cls, info_ann: [str]) -> [DataModel]:
        """
        All the AF of the pop_AF are created

        :param info_ann: Annotations about the variant
        :return: List of AF
        :rtype: [AF]
        """
        try:
            patterns = ["exac", "gnomAD", "1kg", "esp"]
            pops = {}

            for info_a in info_ann:
                for key in info_a:
                    for pattern in patterns:
                        if key.lower().startswith(pattern.lower()):
                            pops[key] = info_a[key]

            AFs = []
            for item in pops.items():
                if item[1] is not None:
                    p = item[0].split('_')
                    if len(p) == 3:
                        af = AlleleFrequency(item[1], p[1], p[0])
                        AFs.append(af)
                    elif len(p) == 2:
                        af = AlleleFrequency(item[1], 'Global', p[0])
                        AFs.append((af))
                    else:
                        raise Exception('Error while Pop_AF creation')
        except Exception:
            AFs = []

        return AFs
