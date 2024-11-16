# Generated by Django 5.1.2 on 2024-11-16 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appQuiz", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="question",
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
                ("question", models.TextField()),
                ("option1", models.CharField(max_length=100)),
                ("option2", models.CharField(max_length=100)),
                ("option3", models.CharField(max_length=100)),
                ("option4", models.CharField(max_length=100)),
                ("correct_option", models.IntegerField()),
            ],
        ),
    ]
