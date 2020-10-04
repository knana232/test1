from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='url_index'),
    path('about/', views.about, name='url_about'),
    path('calculation/',views.cal_wallthickness, name='url_cal_wallthickness'),
]