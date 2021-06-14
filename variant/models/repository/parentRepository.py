
from enum import Enum

class BaseComparator(Enum):
    """
    Enum comparator signs for requests on the database
    """
    EQ = 'eq',
    GT = 'gt',
    GTE = 'gte',
    IN = 'in',
    LT = 'lt',
    LTE = 'lte',
    NE = 'ne',
    NINI = 'nin'

class RepositoryModel():
    """
    Parent class for repository classes
    """
    pass