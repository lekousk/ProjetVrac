# Generated by Django 2.1.5 on 2019-11-20 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20191119_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='adresses',
            field=models.ManyToManyField(to='users.Address'),
        ),
    ]
