# Generated by Django 4.2.2 on 2023-08-03 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='credentials',
            old_name='name',
            new_name='username',
        ),
    ]
