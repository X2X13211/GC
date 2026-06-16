from django.shortcuts import render
from .models import Review


# Create your views here.
# 2.1. Слой контроллеров (reviews/views.py)

# Необходимо разработать функцию-контроллер для обработки запросов к главной странице ленты.

# Фильтрация: Контроллер должен извлекать из БД только те обзоры, у которых статус публикации имеет значение “Истина” (опубликованы).

# Оптимизация (Критическое требование): Примените метод ORM select_related для присоединения данных автора (таблица User) к выборке обзоров в рамках единого SQL-запроса (INNER JOIN).

# Передача данных: Сформируйте контекст (словарь) и передайте извлеченный QuerySet в шаблон.

def review_list(request): 
    reviews = Review.objects.filter(is_published = True).select_related('author')
    context = {'reviews': reviews}
    return render(request, 'reviews/review_list.html', context)
