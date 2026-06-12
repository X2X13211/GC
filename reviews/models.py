from django.db import models
import uuid
from django.utils.text import slugify

# Create your models here.
# Сущность 1: Абстрактная модель аудита (TimeStampedModel)

# Создайте класс TimeStampedModel, наследуемый от базового класса моделей Django (models.Model).

# Поля:

# Дата создания (created_at): Дата и время создания записи. Настройте поле так, чтобы оно автоматически фиксировало время только в момент создания объекта.

# Дата изменения (updated_at): Дата и время изменения записи. Настройте поле так, чтобы оно автоматически обновлялось при каждом сохранении объекта в БД.

# Архитектурное ограничение: Данный класс является вспомогательным и не должен создавать физическую таблицу в базе данных. Опишите мета-параметры класса так, чтобы Django ORM понимал его как абстрактный.

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



# Сущность 2: Основная модель обзора (Review)

# Создайте класс Review, который должен наследоваться от вашей абстрактной модели TimeStampedModel.

# Поля:

# Первичный ключ (id): Переопределите стандартный целочисленный ключ. Используйте тип поля для хранения UUID. Значением по умолчанию должна выступать функция генерации UUID версии 4. Доступ к редактированию этого поля в интерфейсах должен быть жестко заблокирован.

# Заголовок (title): Строковое поле для названия игры (максимальная длина 255 символов).

# URL-слаг (slug): Поле типа SlugField (максимальная длина 255 символов). Наложите на него требование уникальности на уровне СУБД, а также разрешите поддержку кириллических символов (Unicode) для формирования русскоязычных адресов.

# Текст обзора (content): Текстовое поле для хранения основного текста рецензии.

# Статус публикации (is_published): Логическое поле (Boolean), по умолчанию принимающее значение “Опубликовано” (Истина).

class Review(TimeStampedModel):
    id = models.UUIDField(primary_key =True, default=uuid.uuid4, editable= False)
    title = models.CharField(max_length = 255)
    slug = models.SlugField(max_length = 255, unique = True, allow_unicode = True)
    content = models.TextField()
    is_published = models.BooleanField(default = True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
