
import uvicorn

from fastapi import FastAPI

from variant.models.data.parentData import DataModel
from variant.tests.parentTest import ParentTest

HOST = 'localhost'
PORT = 8001

app = FastAPI()

def get_collection(test = False):
    return ParentTest.get_test_collect() if test else DataModel.get_collect()

from variant.web_services.variantScriptWS import *


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=8001)