from django.db import models

# Create your models here.
# python manage.py makemigrations
# python manage.py migrate


class stock_basic(models.Model):
    """
    code,代码
    name,名称
    industry,细分行业
    area,地区
    """

    ts_code = models.CharField(max_length=10, default="000000")
    code = models.CharField(max_length=10, default="000000")
    name = models.CharField(max_length=20, default="无名", blank=True, null=True)
    industry = models.CharField(max_length=100, default="无行业", blank=True, null=True)
    area = models.CharField(max_length=100, default="无地区", blank=True, null=True)
    market = models.CharField(max_length=100, default="无市场类型", blank=True, null=True)
    list_date = models.CharField(max_length=100, default="无上市日期", blank=True, null=True)
    list_status = models.CharField(
        max_length=100, default="无上市状态", blank=True, null=True
    )


class stock_daily(models.Model):
    """
    date,日期
    code,代码
    name,名称
    open,开盘价
    close,收盘价
    low,最低价，
    high,最高价
    volume,成交量，
    turnoverratio,换手率
    changepercent,涨跌幅
    updatetime,更新时间
    """

    ts_code = models.CharField(max_length=100, default="")
    date = models.CharField(max_length=20, default="")
    open = models.FloatField(default=None)
    high = models.FloatField(default=None)
    low = models.FloatField(default=None)
    close = models.FloatField(default=None)
    change = models.FloatField(default=None)
    changepercent = models.FloatField(default=None)
    volume = models.FloatField(default=None)
    amount = models.FloatField(default=None)
    updatetime = models.CharField(max_length=100, default="")

    class Meta:
        unique_together = ["date", "ts_code"]
        # ordering = ['-id']


class stock_ban(models.Model):
    """
    code:
    name:
    date:
    count(万手)
    ratio:解禁后所占比例
    """

    code = models.CharField(max_length=100, default="")
    name = models.CharField(max_length=20, default="")
    date = models.CharField(max_length=20, default="")
    month = models.CharField(max_length=20, default="")
    count = models.FloatField(default=None)
    ratio = models.FloatField(default=None)
