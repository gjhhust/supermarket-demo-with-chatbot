# chatbot/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/response/', views.chatbot_response, name='chatbot_response'), # 定义 API 接口 URL
]