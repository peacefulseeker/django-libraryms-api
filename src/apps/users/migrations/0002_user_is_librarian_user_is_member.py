# Generated by Django 5.0.7 on 2024-07-11 17:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_librarian",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="is_member",
            field=models.BooleanField(default=False),
        ),
    ]