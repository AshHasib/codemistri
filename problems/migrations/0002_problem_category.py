# Generated by Django 2.2.6 on 2019-10-30 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='category',
            field=models.CharField(default='Empty', max_length=100),
            preserve_default=False,
        ),
    ]
