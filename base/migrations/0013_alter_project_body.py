# Generated by Django 3.2.7 on 2021-10-19 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_auto_20211015_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='body',
            field=models.CharField(max_length=200, null=True),
        ),
    ]