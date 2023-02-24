# Generated by Django 4.1.6 on 2023-02-21 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rdv', '0002_auto_20230221_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='client',
            field=models.CharField(default='John Doe', max_length=100),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]
