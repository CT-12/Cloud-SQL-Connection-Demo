from sqlalchemy import Column, Integer, String, DateTime
from marshmallow_sqlalchemy import auto_field, SQLAlchemySchema
from utils.orm_utils import Base
from datetime import datetime

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    price = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now())


class ProductSchema(SQLAlchemySchema):
    class Meta:
        model = Product
        load_instance = True

    id = auto_field(dump_only=True)
    name = auto_field(required=True)
    price = auto_field(required=True)
    created_at = auto_field(dump_only=True)

