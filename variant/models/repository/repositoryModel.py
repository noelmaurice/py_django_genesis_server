
from enum import Enum

class BaseComparator(Enum):
    EQ = 'eq',
    GT = 'gt',
    GTE = 'gte',
    IN = 'in',
    LT = 'lt',
    LTE = 'lte',
    NE = 'ne',
    NINI = 'nin'

class RepositoryModel():
    pass