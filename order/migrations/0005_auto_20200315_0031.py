# Generated by Django 3.0.3 on 2020-03-15 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20200310_0532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subs_platters',
            name='small',
            field=models.FloatField(default=None),
        ),
    ]