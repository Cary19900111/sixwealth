import tushare as ts
from short.config import tushare_token


def basic_data():
    ts.set_token(tushare_token)
    pro = ts.pro_api(tushare_token)
    data = pro.stock_basic(
        exchange="",
        list_status="L",
        fields="ts_code,symbol,name,area,industry,market,list_status,list_date",
    )
    return data


def daily_data(code_list, daytime):
    ts.set_token(tushare_token)
    pro = ts.pro_api(tushare_token)
    data = pro.daily(ts_code=code_list, start_date=daytime, end_date=daytime)
    return data


def month_data():
    ts.set_token(tushare_token)
    pro = ts.pro_api(tushare_token)
    df = pro.monthly(
        trade_date="20211130",
        fields="ts_code,trade_date,open,high,low,close,vol,amount",
    )
    return df
