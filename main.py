from utils.orm_utils import session
import controllers
from models.product import Product, ProductSchema
from utils.logger import logger
logger = logger.getLogger(__name__)
from utils.fake_datas import client_datas_dict, sales_datas_dict

controllers.client.create_many(data=client_datas_dict)
controllers.sale.create_many(data=sales_datas_dict)
logger.info("Created successfully.")