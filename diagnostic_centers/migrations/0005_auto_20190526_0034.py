# Generated by Django 2.2.1 on 2019-05-25 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostic_centers', '0004_auto_20190525_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosticadmin',
            name='password',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='diagnosticadmin',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='diagnosticstaff',
            name='password',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='diagnosticstaff',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
