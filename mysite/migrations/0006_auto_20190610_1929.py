# Generated by Django 2.0.13 on 2019-06-10 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_auto_20190610_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='sex',
            field=models.CharField(max_length=30, null=True),
        ),
    ]