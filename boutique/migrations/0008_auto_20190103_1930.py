# Generated by Django 2.1.3 on 2019-01-03 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0007_auto_20190103_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='proteine',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
