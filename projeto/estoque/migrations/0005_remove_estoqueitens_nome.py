# Generated by Django 2.2.8 on 2020-01-23 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0004_estoqueitens_nome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estoqueitens',
            name='nome',
        ),
    ]