# Generated by Django 2.1.5 on 2019-11-29 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0005_auto_20191129_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prixunite',
            name='ordre_p',
            field=models.IntegerField(verbose_name='Order du produit'),
        ),
        migrations.AlterField(
            model_name='prixunite',
            name='quantite',
            field=models.IntegerField(verbose_name='Quantité du contenant'),
        ),
    ]