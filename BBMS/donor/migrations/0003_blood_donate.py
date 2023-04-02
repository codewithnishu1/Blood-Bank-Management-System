# Generated by Django 4.1.2 on 2022-11-02 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0002_delete_blood_donate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blood_Donate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('bloodgroup', models.CharField(max_length=10)),
                ('unit', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
