# Generated by Django 2.2 on 2019-06-29 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_item_discounted'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='not_discounted',
            field=models.BooleanField(default=True),
        ),
    ]