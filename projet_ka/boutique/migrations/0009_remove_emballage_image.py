# Generated by Django 2.1.5 on 2019-11-29 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0008_auto_20191129_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emballage',
            name='image',
        ),
    ]
