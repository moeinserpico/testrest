# Generated by Django 2.0.2 on 2018-09-30 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_auto_20180928_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amar',
            name='fi',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='فی هر کیلوگرم'),
        ),
    ]