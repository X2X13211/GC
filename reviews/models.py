from django.db import models
import uuid
from django.utils.text import slugify
from django.conf import settings

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
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete = models.CASCADE, 
        related_name = 'reviews', 
        verbose_name = 'Автор'
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
    



