# Generated by Django 3.2.4 on 2021-06-27 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stock_ban',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=100)),
                ('name', models.CharField(default='', max_length=20)),
                ('date', models.CharField(default='', max_length=20)),
                ('month', models.CharField(default='', max_length=20)),
                ('count', models.FloatField(default=None)),
                ('ratio', models.FloatField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='stock_basic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=100)),
                ('name', models.CharField(default='', max_length=20)),
                ('industry', models.CharField(default='', max_length=100)),
                ('area', models.CharField(default='', max_length=100)),
                ('pe', models.FloatField(default=None)),
                ('outstanding', models.FloatField(default=None)),
                ('totals', models.FloatField(default=None)),
                ('totalAssets', models.FloatField(default=None)),
                ('liquidAssets', models.FloatField(default=None)),
                ('fixedAssets', models.FloatField(default=None)),
                ('reserved', models.FloatField(default=None)),
                ('reservedPerShare', models.FloatField(default=None)),
                ('eps', models.FloatField(default=None)),
                ('bvps', models.FloatField(default=None)),
                ('pb', models.FloatField(default=None)),
                ('timeToMarket', models.IntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='stock_daily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='', max_length=20)),
                ('code', models.CharField(default='', max_length=100)),
                ('name', models.CharField(default='', max_length=20)),
                ('open', models.FloatField(default=None)),
                ('close', models.FloatField(default=None)),
                ('low', models.FloatField(default=None)),
                ('high', models.FloatField(default=None)),
                ('volume', models.FloatField(default=None)),
                ('changepercent', models.FloatField(default=None)),
                ('updatetime', models.CharField(default='', max_length=100)),
            ],
            options={
                'unique_together': {('date', 'code')},
                'index_together': {('date', 'code')},
            },
        ),
    ]
