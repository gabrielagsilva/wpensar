# Generated by Django 2.2.11 on 2020-03-11 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='img_url',
        ),
        migrations.AddField(
            model_name='produto',
            name='img',
            field=models.ImageField(default='', upload_to='produtos/<django.db.models.fields.IntegerField>'),
            preserve_default=False,
        ),
    ]
