# Generated by Django 2.0.2 on 2018-09-28 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20180928_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amar',
            name='timestamp',
            field=models.DateField(auto_now_add=True),
        ),
    ]
