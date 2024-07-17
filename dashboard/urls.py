from django.urls import path
from .views import LoginView, DashboardView, logout_view

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('generate_report/', DashboardView.as_view(), name='generate_report'), 
]
