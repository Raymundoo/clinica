# Generated by Django 2.1.5 on 2019-01-15 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cita', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cita',
            name='observacion',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
