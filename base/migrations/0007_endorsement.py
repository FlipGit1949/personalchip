# Generated by Django 3.2.7 on 2021-10-06 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20210924_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endorsement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('body', models.TextField()),
                ('approved', models.BooleanField(default=False, null=True)),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
    ]
