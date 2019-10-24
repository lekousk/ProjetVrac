# Generated by Django 2.1.5 on 2019-10-14 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0014_auto_20191010_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='date_der_modif',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='date de modification'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='date_saisie',
            field=models.DateTimeField(auto_now_add=True, verbose_name="Date d'enregistrement du produit"),
        ),
    ]