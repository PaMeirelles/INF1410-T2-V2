from django.urls import path
from api import views


urlpatterns = [
    path("lista/", views.PostView.as_view(), name='lista-posts'),
    path('umpost/', views.PostView.as_view(), name='um-post'),
    path('umpost/<id_arg>/', views.PostView.as_view(), name='consulta-carro'),

]