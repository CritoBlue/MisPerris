# Generated by Django 2.1.2 on 2018-10-28 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MisPerris', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perro',
            name='persona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='MisPerris.Persona'),
        ),
    ]
