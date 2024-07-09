from .base import BaseController
from models.sale import Sale, SaleSchema

class SaleController(BaseController):
    def __init__(self, model, schema):
        super().__init__(model=model, schema=schema)


sale = SaleController(model=Sale, schema=SaleSchema)