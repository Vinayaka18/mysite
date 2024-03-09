# Generated by Django 4.1.2 on 2024-03-04 05:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0005_alter_try_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("video_source", models.FileField(upload_to="media/videos/")),
                ("thumbnail_image", models.ImageField(upload_to="media/thumbnails/")),
            ],
        ),
    ]