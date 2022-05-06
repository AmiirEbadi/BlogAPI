from django.urls import path, include
from .views import (
    ArticleList,
    ArticleDetail
)

urlpatterns = [
    path('list/', ArticleList.as_view()),
    path('detail/<int:pk>/', ArticleDetail.as_view()),



]