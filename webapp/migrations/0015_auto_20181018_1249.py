# Generated by Django 2.0.2 on 2018-10-18 09:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_mahsool_mtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hazine',
            name='hazineName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.HazineType', verbose_name='نوع'),
        ),
        migrations.AlterField(
            model_name='hazine',
            name='timestamp',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]