# Generated by Django 4.1.7 on 2023-07-17 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=models.TextField(max_length=10000),
        ),
    ]
