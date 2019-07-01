# Generated by Django 2.2 on 2019-06-28 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_item_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='brand',
            field=models.CharField(choices=[('A', 'Apple'), ('G', 'Google'), ('X', 'Xiaomi'), ('SG', 'Samsung'), ('N', 'Nokia'), ('O+', 'OnePlus'), ('Op', 'Oppo'), ('BB', 'Blackberry'), ('SY', 'Sony'), ('H', 'Huawei')], max_length=20),
        ),
    ]
