
import uvicorn
from fastapi import FastAPI

from variant.models.data.parentData import DataModel
from variant.tests.parentTest import ParentTest

"""
HOST : The web service server address
PORT : The web service server communication port
"""
HOST = 'localhost'
PORT = 8001

app = FastAPI()

def get_collection(test = False):
    """
    Return the collection of the database in accordance with tests or not

    @param test: Test mode or not
    @return: Database collection
    @rtype: Collection object
    """
    return ParentTest.get_test_collect() if test else DataModel.get_collect()


"""
The imports below are necessary for runs all webservices
"""

from variant.web_services.variantScriptWS import *


"""
The web service server is launched
"""
if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=8001)