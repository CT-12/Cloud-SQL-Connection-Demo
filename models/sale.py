from utils.orm_utils import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, TIMESTAMP
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from datetime import datetime

class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(String(255), unique=True, nullable=False, comment="訂單編號")
    order_date = Column(String(255), nullable=False, comment="訂單日期")
    shipping_date = Column(String(255), nullable=False, comment="出貨日期")
    delivery_method = Column(String(255), nullable=False, comment="配送方式")
    city = Column(String(255), nullable=False, comment="城市")
    country = Column(String(255), nullable=False, comment="國家")
    product_name = Column(String(255), nullable=False, comment="產品名稱")
    product_type = Column(String(255), nullable=False, comment="產品類別")
    sales_number = Column(Integer, nullable=False, comment="銷售數量")
    sales_amount = Column(Integer, nullable=False, comment="銷售金額")
    profit = Column(Integer, nullable=False, comment="利潤")
    created_at = Column(DateTime, nullable=True, default=datetime.now())
    updated_at = Column(DateTime, nullable=True, default=datetime.now(), onupdate=datetime.now())

    client_id = Column(String(255), ForeignKey("clients.client_id"), nullable=False)


class SaleSchema(SQLAlchemySchema):
    class Meta:
        model = Sale
        load_instance = True


    id = auto_field(dump_only=True)
    order_id = auto_field(required=True)
    order_date = auto_field(required=True)
    shipping_date = auto_field(required=True)
    delivery_method = auto_field(required=True)
    city = auto_field(required=True)
    country = auto_field(required=True)
    product_name = auto_field(required=True)
    product_type = auto_field(required=True)
    sales_number = auto_field(required=True)
    sales_amount = auto_field(required=True)
    profit = auto_field(required=True)
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)

    client_id = auto_field()