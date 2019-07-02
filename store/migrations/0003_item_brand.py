# Generated by Django 2.2 on 2019-06-28 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20190628_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='brand',
            field=models.CharField(choices=[('', 'Apple'), ('', 'Google'), ('', 'Xiaomi'), ('', 'Samsung'), ('', 'Nokia'), ('', 'OnePlus'), ('', 'Oppo'), ('', 'Blackberry'), ('', 'Sony'), ('', 'Huawei')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]