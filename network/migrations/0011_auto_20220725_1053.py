# Generated by Django 3.1.7 on 2022-07-25 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0010_auto_20201105_1053'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['date'], 'verbose_name': 'comment', 'verbose_name_plural': 'comments'},
        ),
    ]