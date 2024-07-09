from .base import BaseController
from models.client import Client, ClientSchema

class ClientController(BaseController):
    def __init__(self, model, schema):
        super().__init__(model=model, schema=schema)


client = ClientController(model=Client, schema=ClientSchema)