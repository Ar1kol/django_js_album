from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('getImages', views.getImages),
    path('posts/',views.ImagesViews.as_view(),name='posts_list'),
    path('getImagesByType/<get_type>', views.getImagesByType),
    
]
