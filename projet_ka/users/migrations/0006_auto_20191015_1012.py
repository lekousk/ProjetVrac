# Generated by Django 2.1.5 on 2019-10-15 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20191015_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='city',
            field=models.CharField(blank=True, max_length=20, verbose_name='ville'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='other_info',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
