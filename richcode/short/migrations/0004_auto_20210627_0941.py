# Generated by Django 3.2.4 on 2021-06-27 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0003_auto_20210627_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_basic',
            name='area',
            field=models.CharField(blank=True, default='无地区', max_length=100),
        ),
        migrations.AlterField(
            model_name='stock_basic',
            name='industry',
            field=models.CharField(blank=True, default='无行业', max_length=100),
        ),
        migrations.AlterField(
            model_name='stock_basic',
            name='list_date',
            field=models.CharField(blank=True, default='无上市日期', max_length=100),
        ),
        migrations.AlterField(
            model_name='stock_basic',
            name='list_status',
            field=models.CharField(blank=True, default='无上市状态', max_length=100),
        ),
        migrations.AlterField(
            model_name='stock_basic',
            name='market',
            field=models.CharField(blank=True, default='无市场类型', max_length=100),
        ),
        migrations.AlterField(
            model_name='stock_basic',
            name='name',
            field=models.CharField(blank=True, default='无名', max_length=20),
        ),
    ]