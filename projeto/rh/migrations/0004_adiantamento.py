# Generated by Django 2.2.8 on 2020-01-01 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0003_saida'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adiantamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('adiantamento', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]