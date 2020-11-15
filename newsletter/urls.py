from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/', views.newsletter_signup, name='newsletter_signup'),
]
