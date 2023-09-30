# Generated by Django 4.2.5 on 2023-09-30 07:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("beatmatcher", "0010_rename_bookingrequest_booking"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="code",
            field=models.CharField(default="", max_length=23),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="booking",
            name="email",
            field=models.EmailField(default="", max_length=254),
            preserve_default=False,
        ),
    ]
