# Generated by Django 3.1.3 on 2022-03-30 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrimeDataSan', '0002_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crimedate',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='crimeposition',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
