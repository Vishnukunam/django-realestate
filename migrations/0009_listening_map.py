# Generated by Django 3.0.7 on 2023-05-22 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0008_delete_send_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='listening',
            name='map',
            field=models.TextField(blank=True),
        ),
    ]