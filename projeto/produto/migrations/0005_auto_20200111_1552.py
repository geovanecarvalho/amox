# Generated by Django 2.2.8 on 2020-01-11 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_produto_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='foto',
            field=models.FileField(blank=True, upload_to='media/'),
        ),
    ]
