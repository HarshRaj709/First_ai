from django.urls import path
from . import views

urlpatterns = [
    path('',views.form,name='home'),
    path('result/',views.result,name='result')
]
