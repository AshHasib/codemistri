# Generated by Django 2.2.6 on 2019-10-30 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0006_auto_20191030_0657'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='difficulty',
            field=models.TextField(default='easy', max_length=100),
            preserve_default=False,
        ),
    ]
