from django.urls import path
from blog import views

urlpatterns = [
    path("lista/", views.PostView.as_view(), name='lista-posts')
]