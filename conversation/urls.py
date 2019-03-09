

from django.urls import path
from conversation import views

urlpatterns = [
    path('sentence/', views.sentence_list),
]