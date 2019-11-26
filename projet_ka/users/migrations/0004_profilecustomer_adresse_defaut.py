# Generated by Django 2.1.5 on 2019-11-22 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profilecustomer_newsletter'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilecustomer',
            name='adresse_defaut',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='selected_address', to='users.Address'),
        ),
    ]