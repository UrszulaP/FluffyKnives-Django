# Generated by Django 2.1.5 on 2019-07-07 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190120_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='itemImage',
            field=models.ImageField(upload_to='items_pics'),
        ),
    ]