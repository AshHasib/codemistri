# Generated by Django 2.2.6 on 2019-10-30 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0005_auto_20191030_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='category',
            field=models.TextField(max_length=100),
        ),
    ]