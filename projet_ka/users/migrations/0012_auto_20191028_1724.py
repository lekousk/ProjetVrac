# Generated by Django 2.1.5 on 2019-10-28 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20191028_1707'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='date_of_birth',
            new_name='birth_date',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='adress',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='adresse'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='city',
            field=models.CharField(blank=True, max_length=30, verbose_name='ville'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='other_info',
            field=models.CharField(blank=True, max_length=50, verbose_name='informations complémentaires'),
        ),
    ]