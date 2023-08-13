from django.urls import path

from .views import show_user, registration

urlpatterns = [
    path('user/<int:pk>/', show_user, name='show_the_user'),
    path('registration/', registration, name='registration')
]