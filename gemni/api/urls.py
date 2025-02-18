from django.urls import path
from . import views


urlpatterns = [
    path('plan/',views.form.as_view(),name='travel_suggestions'),
    path('history/',views.UserSearch.as_view(),name ='history')
]