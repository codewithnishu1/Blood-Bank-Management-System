# Generated by Django 4.1.2 on 2022-10-29 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='patient',
            name='mobile_no',
            field=models.PositiveIntegerField(),
        ),
    ]
