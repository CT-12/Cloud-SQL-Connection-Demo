import pandas as pd
from .logger import logger
import logging
logger = logger.getLogger(__name__)
logger.setLevel(logging.ERROR)
import os

logger.info(f"Current pwd: {os.getcwd()}")

def map_keys(original: list[dict], mapping: dict) -> list[dict]:
    return [{mapping.get(key, key): value for key, value in dic.items()} for dic in original]


file_path = "./utils/dataset/銷售資料.xlsx"

mapping_dict = {
    "客戶編號": "client_id",
    "客戶名稱": "client_name",
    "客戶地址": "address",
}
client_datas_df: pd.DataFrame = pd.read_excel(file_path, sheet_name="客戶")
client_datas_df = client_datas_df.rename(columns=mapping_dict)
client_datas_dict: list[dict] = client_datas_df.to_dict(orient="records")


mapping_dict = {
    "訂單編號": "order_id",
    "訂單日期": "order_date",
    "出貨日期": "shipping_date",
    "配送方式": "delivery_method",
    "客戶編號": "client_id",	
    "城市": "city",
    "國家": "country",	
    "產品名稱": "product_name",
    "產品類別": "product_type",	
    "銷售數量": "sales_number",	
    "銷售金額": "sales_amount",	
    "商品利潤": "profit",
}
sales_datas_df: pd.DataFrame = pd.read_excel(file_path, sheet_name="銷售資料")
sales_datas_df = sales_datas_df.rename(columns=mapping_dict)
sales_datas_df["order_date"] = sales_datas_df["order_date"].astype(str)
sales_datas_df["shipping_date"] = sales_datas_df["shipping_date"].astype(str)
sales_datas_dict: list[dict] = sales_datas_df.to_dict(orient="records")
