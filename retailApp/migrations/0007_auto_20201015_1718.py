# Generated by Django 3.1.2 on 2020-10-15 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retailApp', '0006_auto_20201015_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='image'),
        ),
    ]
