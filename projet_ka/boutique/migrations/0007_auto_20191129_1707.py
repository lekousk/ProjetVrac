# Generated by Django 2.1.5 on 2019-11-29 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0006_auto_20191129_1651'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categorie_mere',
            new_name='CategorieMere',
        ),
        migrations.RenameModel(
            old_name='Categorie_produit',
            new_name='CategorieProduit',
        ),
    ]