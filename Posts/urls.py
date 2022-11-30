from django.urls import path
from . import views

app_name = 'djangoProject1'

urlpatterns = [
    path("", views.index, name= "index"),
    path("<int:post_id>/", views.post_detail, name = "post-detail"),
]