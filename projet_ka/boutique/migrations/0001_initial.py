# Generated by Django 2.1.3 on 2018-11-22 16:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_du_produit', models.CharField(max_length=100)),
                ('categorie', models.CharField(max_length=100)),
                ('prix_produit', models.FloatField()),
                ('type_du_prix', models.BooleanField()),
                ('date_saisie', models.DateTimeField(default=django.utils.timezone.now, verbose_name="Date d'enregistrement du produit")),
                ('description', models.TextField()),
                ('image_produit', models.ImageField(upload_to='image_produit/')),
            ],
            options={
                'verbose_name': 'produit',
                'ordering': ['date_saisie'],
            },
        ),
    ]