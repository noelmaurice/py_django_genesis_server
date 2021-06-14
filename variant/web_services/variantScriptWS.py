from variant.models.repository.variantRepository import VariantRepository
from variant.web_services.data.variantWS import VariantWS

from variant.web_services.mainScriptWS import app, get_collection


@app.post('/variant/')
async def create_variant(variant_ws: VariantWS, test: bool = False):

    variant = variant_ws.toData()

    id = VariantRepository.create(variant, collect=get_collection(test))

    return {'id': id}


@app.get('/variant/filters/')
async def find_distinct_filters(sample_name: str, test: bool = False):

    filters = VariantRepository.find_distinct_filters(sample_name, collect=get_collection(test))

    return {'filters': filters}


@app.get('/variant/node_value/')
async def find_node_contains_value(sample_name: str, node: str, value: str, test: bool = False):

    variants = VariantRepository.find_variants_node_value(sample_name, node, [value], collect=get_collection(test))

    return variants


@app.get('/variant/frequency/')
async def find_variants_with_frequency(sample_name: str, frequency: float, operator:str = None, test: bool = False):

    variants = VariantRepository.find_variants_frequency(sample_name, frequency, operator, collect=get_collection(test))

    return variants
