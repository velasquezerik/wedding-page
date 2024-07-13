from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('download/<uuid:photo_id>/', views.download, name='download'),
    path('upload/', views.image_upload_view, name='upload'),
]
