from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from short.models import stock_basic, stock_daily, stock_ban
import tushare as ts
from short.utils.get_datas import *
import datetime


def basicElementExist(stock_code):
    try:
        stock_basic.objects.get(code=stock_code)
        return True
    except Exception as err:
        return False


def test(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def basic(request):
    """L上市 D退市 P暂停上市"""
    df = get_basic_data()
    code_list = df.index.tolist()
    for index in code_list:
        ts_code = df.loc[index, "ts_code"]
        code = df.loc[index, "symbol"]
        name = df.loc[index, "name"]
        industry = df.loc[index, "industry"]
        area = df.loc[index, "area"]
        market = df.loc[index, "market"]
        list_status = df.loc[index, "list_status"]
        list_date = df.loc[index, "list_date"]

        if basicElementExist(code):
            stock_basic.objects.filter(code=code).update(
                ts_code=ts_code,
                name=name,
                industry=industry,
                area=area,
                market=market,
                list_status=list_status,
                list_date=list_date,
            )
        else:
            q = stock_basic(
                ts_code=ts_code,
                code=code,
                name=name,
                industry=industry,
                area=area,
                market=market,
                list_status=list_status,
                list_date=list_date,
            )
            q.save()
    return HttpResponse("basic information sync Done!")


def daily(request):
    """获取share的日数据"""
    daytime = request.GET["daytime"]
    updatetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ts_code_list = []
    ts_code_partion = []
    partion_index = 0
    ts_codes = stock_basic.objects.values_list("ts_code")
    for ts_code in ts_codes:
        ts_code_partion.append(ts_code[0])
        partion_index = partion_index + 1
        if partion_index == 50:
            ts_code_list.append(ts_code_partion)
            partion_index = 0
            ts_code_partion = []
    ts_code_partion.append(ts_code_partion)
    for ts_code_partition in ts_code_list:
        df = get_daily_data(",".join(ts_code_partition), daytime)
        code_list = df.index.tolist()
        for index in code_list:
            ts_code = df.loc[index, "ts_code"]
            open = df.loc[index, "open"]
            close = df.loc[index, "close"]
            low = df.loc[index, "low"]
            high = df.loc[index, "high"]
            change = df.loc[index, "change"]
            pct_chg = df.loc[index, "pct_chg"]
            vol = df.loc[index, "vol"]
            amount = df.loc[index, "amount"]
            q = stock_daily(
                date=daytime,
                ts_code=ts_code,
                open=open,
                close=close,
                low=low,
                high=high,
                change=change,
                changepercent=pct_chg,
                volume=vol,
                amount=amount,
                updatetime=updatetime,
            )
            try:
                q.save()
            except Exception as err:
                print(str(err))
                print(ts_code)
    return HttpResponse("{} daily information sync Done!".format(daytime))
