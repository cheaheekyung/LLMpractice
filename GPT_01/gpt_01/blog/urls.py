from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("list/", views.list, name="list"),
    path("create/", views.create, name="create"),
    path("<int:pk>/detail/", views.detail, name="detail"),
]
