# Generated by Django 3.1.2 on 2020-10-10 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retailApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
