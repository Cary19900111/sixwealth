from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from tushare import stock
from short.models import stock_basic, stock_daily, stock_ban
import tushare as ts
from short.utils.get_datas import *
import datetime


def test(request):
    pass


def code_to_basic(code_list):
    results = []
    basics = stock_basic.objects.filter(ts_code__in=code_list).values()
    for basic in basics:
        basic_list = []
        code = basic["code"]
        name = basic["name"]
        industry = basic["industry"]
        area = basic["area"]
        basic_list.append(code)
        basic_list.append(name)
        basic_list.append(industry)
        basic_list.append(area)
        results.append(basic_list)
    return results


def basicElementExist(stock_code):
    try:
        stock_basic.objects.get(code=stock_code)
        return True
    except Exception as err:
        return False


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


def volumn_donw(request):
    """volumn_donw"""
    stock_list = []
    code_list = stock_basic.objects.values("ts_code").distinct()
    # code_list = [{'code':'600716'}]
    for code_dic in code_list:
        try:
            code1 = code_dic["ts_code"]
            code1_daily_datas = (
                stock_daily.objects.filter(ts_code=code1)
                .order_by("id")
                .reverse()[:2]
                .values()
            )
            data_list = list(code1_daily_datas)
            volume_today = data_list[0]["volume"]
            volume_pre = data_list[1]["volume"]
            open_today = data_list[0]["open"]
            close_today = data_list[0]["close"]
            # data_list[0]['date'] != date_today or
            if (
                volume_today == 0
                or data_list[0]["changepercent"] > 8.0
                or data_list[0]["changepercent"] < -8.0
            ):
                continue
            if close_today <= open_today and volume_today <= 0.4 * volume_pre:
                stock_list.append(code1)
        except Exception as err:
            print("error:" + str(err))
            continue
    print(stock_list)
    return HttpResponse("bottom red 2 calculate done!")


def deepv_add_two_high(request):
    """深V,持续2天创新高"""
    stock_list = []
    code_list = stock_basic.objects.values("ts_code").distinct()
    # code_list = [{'code':'600716'}]
    for code_dic in code_list:
        try:
            code1 = code_dic["ts_code"]
            code1_daily_datas = (
                stock_daily.objects.filter(ts_code=code1)
                .order_by("id")
                .reverse()[0:3]
                .values()
            )
            data_list = list(code1_daily_datas)
            one_open = data_list[2]["open"]
            one_low = data_list[2]["low"]
            one_close = data_list[2]["close"]
            one_high = data_list[2]["high"]
            two_high = data_list[1]["high"]
            three_high = data_list[0]["high"]
            # data_list[0]['date'] != date_today or
            if (
                (one_open - one_low) / one_low > 0.05
                and (one_close - one_low) / one_low > 0.05
                and two_high > one_high
                and three_high > two_high
            ):
                stock_list.append(code1)
        except Exception as err:
            print("error:" + str(err))
            continue
    basic_info = code_to_basic(stock_list)
    result = ""
    for info in basic_info:
        result = result + str(info) + "\n"
    print(result)
    return HttpResponse("deep_v done!")
