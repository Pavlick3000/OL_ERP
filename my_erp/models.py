from django.db import models

class TableOl(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.TextField(db_column='Name', verbose_name="Имя пользователя")  # Field name made lowercase.
    email = models.TextField(db_column='Email', verbose_name="Почтовый ящик", unique=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', verbose_name="Возраст")  # Field name made lowercase.

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ol'
        verbose_name = "Таблица ol"
        verbose_name_plural = "Таблица ol" # - представление во множественном числе
        ordering = ['name']
