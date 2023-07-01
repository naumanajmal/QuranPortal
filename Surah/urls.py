from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("script/", views.main, name="main"),
    path('update_row/<int:row_id>/', views.update_row, name='update_row'),
]