# Generated by Django 4.0.4 on 2023-04-22 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PrimeraApp', '0002_alter_entregables_fechadeentrega'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='comicion',
            new_name='comision',
        ),
    ]
