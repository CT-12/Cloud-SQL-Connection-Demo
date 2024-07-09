from utils.orm_utils import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from marshmallow_sqlalchemy import auto_field, SQLAlchemySchema
from datetime import datetime
from .sale import Sale

class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(String(255), unique=True, nullable=False, comment="客戶編號")
    client_name = Column(String(255), nullable=False, comment="客戶名稱")
    address = Column(String(255), nullable=False, comment="住址")
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.now(), default=datetime.now())

    # lazy 是在是當叫出某個屬性時才會去資料去讀取，所以如果存取該屬性時沒有 session 存在的話就會報錯
    # 這也是 get_one() 那邊沒有 session.close() 的原因，close 就不能存取屬性了！！！
    sales = relationship("Sale", backref="clients", uselist=True, lazy=True)


class ClientSchema(SQLAlchemySchema):
    class Meta:
        model = Client
        load_instance = True

    id = auto_field(dump_only=True)
    client_id = auto_field(required=True)
    client_name = auto_field(required=True)
    address = auto_field(required=True)
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)

    sales = auto_field()