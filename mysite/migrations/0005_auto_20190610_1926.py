# Generated by Django 2.0.13 on 2019-06-10 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20190610_1841'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='data',
            options={'ordering': ['-enroll_date']},
        ),
        migrations.AlterField(
            model_name='data',
            name='deal_type',
            field=models.CharField(help_text='거주유형', max_length=100),
        ),
        migrations.AlterField(
            model_name='data',
            name='deposit',
            field=models.CharField(help_text='보증금', max_length=200),
        ),
        migrations.AlterField(
            model_name='data',
            name='monthly_price',
            field=models.CharField(help_text='월세', max_length=200),
        ),
        migrations.AlterField(
            model_name='data',
            name='residence_type',
            field=models.CharField(help_text='건물형태', max_length=100),
        ),
        migrations.AlterField(
            model_name='data',
            name='sex',
            field=models.CharField(choices=[('m', '남자'), ('f', '여자')], max_length=1, null=True),
        ),
    ]
