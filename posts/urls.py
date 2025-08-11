from django.urls import path
from django.views.decorators.csrf import csrf_exempt


from .views import PostList, PostDetail, ContactCreate

urlpatterns = [

path('posts/', PostList.as_view()),
path('posts/<int:pk>/',PostDetail.as_view()),
path('contact/', csrf_exempt(ContactCreate.as_view())),
]