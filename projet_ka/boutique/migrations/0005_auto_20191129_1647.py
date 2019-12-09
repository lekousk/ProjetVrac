# Generated by Django 2.1.5 on 2019-11-29 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0004_auto_20191129_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrixUnite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordre_p', models.IntegerField(max_length=2, verbose_name='Order du produit')),
                ('quantite', models.IntegerField(max_length=7, verbose_name='Quantité du contenant')),
            ],
            options={
                'ordering': ['produit', 'ordre_p'],
            },
        ),
        migrations.AddField(
            model_name='emballage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='boutique/image_produit/', verbose_name="Image de l'emballage"),
        ),
        migrations.AlterField(
            model_name='producteur',
            name='image_prod',
            field=models.ImageField(blank=True, null=True, upload_to='boutique/image_producteur/', verbose_name='Image du producteur'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='image_p',
            field=models.ImageField(blank=True, null=True, upload_to='boutique/image_produit/', verbose_name='Image du produit'),
        ),
        migrations.AddField(
            model_name='prixunite',
            name='emballage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emballage', to='boutique.Emballage'),
        ),
        migrations.AddField(
            model_name='prixunite',
            name='produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prix_unite', to='boutique.Produit'),
        ),
    ]
