from django.urls import path
from .views import article_details,ArticleAPIView, ArticleDetails, GenericAPIView

urlpatterns = [
    # path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    # GenericAPIView
     path('generic/article/<int:id>/', GenericAPIView.as_view()),
    path('detail/<int:id>/',ArticleDetails.as_view())
    # path ('detail/<int:pk>/', article_details)
]
