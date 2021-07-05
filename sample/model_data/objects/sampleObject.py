from datetime import datetime
from typing import List

from sample.model_data.objects.parentObject import ParentObject

class PartObject(ParentObject):

    def __init__(self,
                 id: int,
                 name: str,
                 value: str):

        self.id = id
        self.name = name
        self.value = value

    def __str__(self):
        return '{} - {}'.format(self.name, self.value)



class SampleObject(ParentObject):

    def __init__(self,
                 id: int,
                 name: str,
                 filters: List[str],
                 parts: List[PartObject],
                 pub_date: datetime = datetime.now()):

        self.id = id
        self.name = name
        self.pub_date = pub_date
        self.parts = parts
        self.filters = filters

    def __str__(self):
        return '{} ({})'.format(self.name, self.id)



