# Generated by Django 4.2.1 on 2023-06-29 00:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ReneApp", "0003_meme_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="meme",
            name="upload_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
