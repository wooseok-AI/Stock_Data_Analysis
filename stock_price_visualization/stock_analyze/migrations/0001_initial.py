# Generated by Django 4.2 on 2023-05-02 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=50)),
                ('listing_date', models.DateField()),
                ('dividend_date', models.DateField(null=True)),
                ('dividend_amount', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('open_price', models.IntegerField()),
                ('close_price', models.IntegerField()),
                ('high_price', models.IntegerField()),
                ('low_price', models.IntegerField()),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock_analyze.stock')),
            ],
        ),
    ]
