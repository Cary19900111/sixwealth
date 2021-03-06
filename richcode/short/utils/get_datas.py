from short.components.data_from_tushare import basic_data, daily_data, month_data


def get_basic_data():
    return basic_data()


def get_daily_data(code_list, begintime, endtime):
    return daily_data(code_list, begintime, endtime)


def get_month_data(yymm):
    return month_data(yymm)
