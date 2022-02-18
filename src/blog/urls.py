from django.urls import path
from . import views
from .views import PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('detail/<int:post_id>/', views.post_detail, name='detail'),

    path('new-post/', PostCreateView.as_view(), name='new_post'),
    path('detail/update-post/<slug:pk>/', PostUpdateView.as_view(), name='update_post'),
    path('detail/delete-post/<slug:pk>/', PostDeleteView.as_view(), name='delete_post'),


]