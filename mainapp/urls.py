from django.urls import path

from mainapp.views import get_only_one_page

urlpatterns = [
    path('', get_only_one_page)
]