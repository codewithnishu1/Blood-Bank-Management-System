# Generated by Django 4.1.2 on 2022-10-29 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bloodmanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='admini',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('units', models.PositiveIntegerField()),
                ('Bgroup', models.CharField(max_length=3)),
                ('status', models.CharField(default='Pending', max_length=50)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='blood_request',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]