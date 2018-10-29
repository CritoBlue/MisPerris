# Generated by Django 2.1.2 on 2018-10-29 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MisPerris', '0005_auto_20181029_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='bday',
            field=models.DateField(verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='email',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='persona',
            name='tel',
            field=models.CharField(max_length=9),
        ),
    ]