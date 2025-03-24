from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('detail_vacancy/<int:vacancy_id>/', views.detail_vacancy, name='detail_vacancy'),
]