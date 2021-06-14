"""
Variant web services
"""

from variant.models.repository.variantRepository import VariantRepository
from variant.web_services.data.variantWS import VariantWS

from variant.web_services.mainScriptWS import app, get_collection


@app.post('/variant/')
async def create_variant(variant_ws: VariantWS, test: bool = False):
    """
    The variant is saved in the database

    @param variant_ws: Variant to save
    @param test: Test mode
    @return: Id of the variant saved
    @rtype: str
    """
    variant = variant_ws.toData()

    id = VariantRepository.create(
        variant,
        collect=get_collection(test))

    return {'id': id}


@app.get('/variant/filters/')
async def find_distinct_filters(sample_name: str, test: bool = False):
    """
    For a sample, the distinct filters are searched
    @param sample_name: Sample name
    @param test: Test mode
    @return: The filters found
    @rtype: list(str)
    """
    filters = VariantRepository.find_distinct_filters(
        sample_name,
        collect=get_collection(test))

    return {'filters': filters}


@app.get('/variant/node_value/')
async def find_node_contains_value(
        sample_name: str,
        node: str,
        value: str,
        test: bool = False):
    """
    Search variants with the value for the variant node

    @param sample_name: Sample name
    @param node: The node on which the search is made
    @param value: The searched value for the node
    @param test: Test mode
    @return: The variants found
    @rtype: list(Variant)
    """
    variants = VariantRepository.find_variants_node_value(
        sample_name,
        node, [value],
        collect=get_collection(test))

    return variants


@app.get('/variant/frequency/')
async def find_variants_with_frequency(
        sample_name: str,
        frequency: float,
        operator:str = None,
        test: bool = False):
    """
    Search the variant in accordance with the frequency value

    @param sample_name: Sample name
    @param frequency: The frequency value searched
    @param operator: The comparison operator
    @param test: Mode test
    @return: The variants found
    @rtype: list(Variant)
    """
    variants = VariantRepository.find_variants_frequency(
        sample_name,
        frequency,
        operator,
        collect=get_collection(test))

    return variants
