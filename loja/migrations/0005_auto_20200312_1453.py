# Generated by Django 2.2.11 on 2020-03-12 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0004_auto_20200311_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nivel',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='senha',
            field=models.CharField(default='', max_length=16),
        ),
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='produtos'),
        ),
    ]