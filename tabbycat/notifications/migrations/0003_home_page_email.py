# Generated by Django 2.0.5 on 2018-07-17 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_rename_recipient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagesentrecord',
            name='event',
            field=models.CharField(choices=[('p', 'team points'), ('c', 'ballot confirmed'), ('f', 'feedback URL'), ('b', 'ballot URL'), ('u', 'splash page URL')], max_length=1, verbose_name='event'),
        ),
    ]
