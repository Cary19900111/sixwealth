from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from short.models import stock_basic, stock_daily, stock_ban
import tushare as ts
from short.utils.get_datas import *


def basicElementExist(stock_code):
    try:
        obj = stock_basic.objects.get(code=stock_code)
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
        code = df.loc[index, "symbol"]
        name = df.loc[index, "name"]
        industry = df.loc[index, "industry"]
        area = df.loc[index, "area"]
        market = df.loc[index, "market"]
        list_status = df.loc[index, "list_status"]
        list_date = df.loc[index, "list_date"]

        if basicElementExist(code):
            stock_basic.objects.filter(code=code).update(
                name=name,
                industry=industry,
                area=area,
                market=market,
                list_status=list_status,
                list_date=list_date,
            )
        else:
            q = stock_basic(
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
