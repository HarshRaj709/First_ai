from django.urls import path
from . import views


urlpatterns = [
    path('',views.form.as_view(),name='travel_suggestions'),
]