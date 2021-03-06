# Generated by Django 2.1.5 on 2019-11-25 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profilecustomer_adresse_defaut'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'ordering': ['user', 'id']},
        ),
        migrations.AddField(
            model_name='myuser',
            name='genre',
            field=models.CharField(choices=[('M', 'Monsieur'), ('Mme', 'Madame'), ('Mlle', 'Mademoiselle')], default='M', max_length=5, verbose_name='Civilité'),
            preserve_default=False,
        ),
    ]
