# Generated by Django 3.2.4 on 2021-06-27 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock_basic',
            name='bvps',
        ),
        migrations.RemoveField(
            model_name='stock_basic',
            name='eps',
        ),
        migrations.RemoveField(
            model_name='stock_basic',
            name='fixedAssets',
        ),
        migrations.RemoveField(
            model_name='stock_basic',
            name='liquidAssets',
        ),
        migrations.RemoveField(
            model_name='stock_basic',
            name='outstanding',
        ),
        migrations.RemoveField(
            model_name='stock_basic',
            name='pb',
        ),
        migrations.RemoveField(
            model_name='stock_basic',
            name='pe',
        ),
        migrations.RemoveField(
            model_name='stock_basic',
            name='reserved',
        ),
        migrations.RemoveField(
            model_name='stock_basic',
            name='reservedPerShare',
        ),
        migrations.RemoveField(
            model_name='stock_basic',
            name='timeToMarket',
        ),
        migrations.RemoveField(
            model_name='stock_basic',
            name='totalAssets',
        ),
        migrations.RemoveField(
            model_name='stock_basic',
            name='totals',
        ),
        migrations.AddField(
            model_name='stock_basic',
            name='list_date',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='stock_basic',
            name='list_status',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='stock_basic',
            name='market',
            field=models.CharField(default='', max_length=100),
        ),
    ]
