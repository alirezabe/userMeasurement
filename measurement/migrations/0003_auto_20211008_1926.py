# Generated by Django 3.2.8 on 2021-10-08 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_alter_measurement_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='height',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='weight',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='width',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
