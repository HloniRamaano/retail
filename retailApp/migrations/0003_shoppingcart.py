# Generated by Django 3.1.2 on 2020-10-10 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retailApp', '0002_product_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]