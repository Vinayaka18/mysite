# Generated by Django 4.1.2 on 2024-03-04 05:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0006_video"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Video",
            new_name="HtmlVideo",
        ),
    ]