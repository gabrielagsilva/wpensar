# Generated by Django 2.2.11 on 2020-03-14 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0002_auto_20200314_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='total',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]