from django.urls import path
from .views import popular, singlepost, write, update, delete,LikeView, writecomment, number_user

urlpatterns = [
    path('popular/',popular.as_view(),name="popular"),
    path('post/<int:pk>',singlepost.as_view(),name="singlepost"),
    path('write/',write.as_view(),name="write"),
    path('update/<int:pk>',update.as_view(),name="update"),
    path('delete/<int:pk>',delete.as_view(),name="delete"),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('post/<int:pk>/comment/', writecomment.as_view(), name='write_comment'),
    path('num_user/', number_user, name='number_user'),
]