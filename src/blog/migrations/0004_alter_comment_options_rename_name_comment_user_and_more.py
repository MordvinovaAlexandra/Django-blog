# Generated by Django 5.0.2 on 2024-02-13 16:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_comment"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ["-created"]},
        ),
        migrations.RenameField(
            model_name="comment",
            old_name="name",
            new_name="user",
        ),
        migrations.AddIndex(
            model_name="comment",
            index=models.Index(
                fields=["-created"], name="blog_commen_created_79f39f_idx"
            ),
        ),
    ]