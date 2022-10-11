from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(verbose_name="Метка", max_length=250, unique=True)

    class Meta:
        verbose_name = "Метка"
        verbose_name_plural = "Список меток"

    def __str__(self):
        return self.name


class Item(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Название задачи", max_length=250)
    description = models.TextField(verbose_name="Описание задачи", blank=True)
    priority = models.IntegerField(verbose_name="Приоритет сортировки", default=1, db_index=True)
    done = models.DateTimeField(verbose_name="Выполнено", blank=True, null=True)
    created = models.DateTimeField(verbose_name="Создано", auto_now_add=True, db_index=True)
    updated = models.DateTimeField(verbose_name="Изменено", auto_now=True)
    tag = models.ManyToManyField(Tag, verbose_name="Метки", blank=True)

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Список задач"
        ordering = ("priority", "created")

    def __str__(self):
        return self.name

