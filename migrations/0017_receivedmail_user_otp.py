# Generated by Django 3.0.7 on 2023-05-25 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0016_delete_receivedotpmail'),
    ]

    operations = [
        migrations.AddField(
            model_name='receivedmail',
            name='user_otp',
            field=models.CharField(blank=True, max_length=4),
        ),
    ]
