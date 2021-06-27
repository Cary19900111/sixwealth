import tushare as ts
from short.config import tushare_token


def basic_data():
    ts.set_token(tushare_token)
    pro = ts.pro_api(tushare_token)
    data = pro.stock_basic(
        exchange="",
        list_status="L",
        fields="symbol,name,area,industry,market,list_status,list_date",
    )
    return data
