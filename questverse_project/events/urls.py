from django.urls import path
from .views import dashboard, login_page

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('', login_page, name='login'),
]