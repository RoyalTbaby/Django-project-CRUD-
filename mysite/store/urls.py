from django.urls import path
from . views import user_list
from .views import MyFormView
from django.urls import path
from . import views

urlpatterns = [
    path('', user_list, name='home'),
    path('form/', MyFormView.as_view(), name='form'),
    path('user/<int:pk>/', views.user_detail, name='user_detail'),
    path('user/<int:pk>/edit/', views.user_edit, name='user_edit'),
    path('user/<int:pk>/delete/', views.user_delete, name='user_delete')
]