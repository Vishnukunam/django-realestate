# Generated by Django 3.0.7 on 2023-05-23 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0012_sendmail'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sendmail',
            new_name='ReceivedMail',
        ),
    ]