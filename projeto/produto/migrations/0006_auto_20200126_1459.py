# Generated by Django 2.2.8 on 2020-01-26 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0005_auto_20200111_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='foto',
            field=models.FileField(blank=True, upload_to='media/produtos'),
        ),
    ]
