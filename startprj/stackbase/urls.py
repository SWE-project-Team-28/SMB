from django.urls import path
from . import views

app_name = 'stackbase'

urlpatterns = [
    path('', views.QuestionListView.as_view(), name="question-lists"),
    
    # CRUD Function
    # path('questions/', views.QuestionListView.as_view(), name="question-lists"),
    path('questions/new/', views.QuestionCreateView.as_view(), name="question-create"),

]
