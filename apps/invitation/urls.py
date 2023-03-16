from django.urls import path

from . import views

app_name = 'invitation'
urlpatterns = [
    # ex: /invitation/
    path('', views.index, name='index'),
    # ex: /invitation/5/
    path('<uuid:invitation_id>/', views.detail, name='detail'),
    # ex: /invitation/5/confirm/
    path('<uuid:invitation_id>/confirm/', views.confirm, name='confirm'),
]