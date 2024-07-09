from models.product import Product, ProductSchema
from .base import BaseController

class ProductController(BaseController):
    def __init__(self, model, schema):
        super().__init__(model=model, schema=schema)
        

product = ProductController(model=Product, schema=ProductSchema)