from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.review_list, name='review_list'),
]
# 2.2. Маршрутизация (urls.py)

# Локальный маршрутизатор: В приложении reviews создайте файл urls.py. Зарегистрируйте 
# маршрут для пустого пути (''), указывающий на созданный контроллер. Обязательно задайте пространство имен 
# (app_name = 'reviews').

# Глобальный маршрутизатор: В главном файле config/urls.py удалите временный TemplateView 
# (если он использовался ранее для заглушки главной страницы) и подключите локальные маршруты приложения reviews с 
# помощью функции include.
