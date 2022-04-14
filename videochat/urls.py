from django.urls import path
from videochat import views

app_name = 'videochat'

urlpatterns = [
    path('videochatlobby/', views.videochatlobbyviews, name='lobby'),
    path('videochatroom/', views.videochatroomviews, name='room'),
    path('get_token/', views.getToken),
]