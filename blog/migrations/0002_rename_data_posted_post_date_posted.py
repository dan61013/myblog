# Generated by Django 5.1.3 on 2025-03-28 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="data_posted",
            new_name="date_posted",
        ),
    ]
