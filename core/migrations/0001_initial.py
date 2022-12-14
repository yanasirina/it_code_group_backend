# Generated by Django 4.1.2 on 2022-10-11 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                (
                    "name",
                    models.CharField(max_length=250, unique=True, verbose_name="Метка"),
                ),
            ],
            options={
                "verbose_name": "Метка",
                "verbose_name_plural": "Список меток",
            },
        ),
        migrations.CreateModel(
            name="Item",
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
                (
                    "name",
                    models.CharField(max_length=250, verbose_name="Название задачи"),
                ),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="Описание задачи"),
                ),
                (
                    "priority",
                    models.IntegerField(
                        db_index=True, default=1, verbose_name="Приоритет сортировки"
                    ),
                ),
                (
                    "done",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Выполнено"
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="Создано"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True, verbose_name="Изменено"),
                ),
                (
                    "tag",
                    models.ManyToManyField(
                        blank=True, to="core.tag", verbose_name="Метки"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Задача",
                "verbose_name_plural": "Список задач",
                "ordering": ("priority", "created"),
            },
        ),
    ]
