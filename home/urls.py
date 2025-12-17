from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('blog/<int:blog_id>/', views.get_blogs, name='get_blogs'),
]
