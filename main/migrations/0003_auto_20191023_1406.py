# Generated by Django 2.2.6 on 2019-10-23 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191023_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rank',
            field=models.CharField(blank=True, default='noob', max_length=10),
            preserve_default=False,
        ),
    ]
