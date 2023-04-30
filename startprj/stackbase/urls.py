from django.urls import path
from . import views

app_name = 'stackbase'

urlpatterns = [
    path('', views.QuestionListView.as_view(), name="question-lists"),
    
    # CRUD Function
    # path('questions/', views.QuestionListView.as_view(), name="question-lists"),
    path('questions/new/', views.QuestionCreateView.as_view(), name="question-create"),
    
    path('questions/<int:pk>/<str:tag_name>/',views.QuestionListByTagView.as_view(),name="question-tag"),
    path('tags/<str:tag_name>/',views.QuestionListByTagView.as_view(),name="tag-question"),
    path('tags/', views.TagListView.as_view(), name='tag-list'),

]
