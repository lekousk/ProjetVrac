# Generated by Django 2.1.5 on 2019-10-28 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20191028_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='city',
            field=models.CharField(blank=True, max_length=20, verbose_name='city'),
        ),
    ]