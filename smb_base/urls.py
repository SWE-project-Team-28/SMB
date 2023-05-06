from django.urls import path
from . import views

app_name = 'smb_base'
urlpatterns = [
    path('', views.Question_List_View.as_view(), name="question-lists"),
    
    path('questions/new/', views.Question_Create_View.as_view(), name="question-create"),
    path('questions/<int:pk>/', views.Question_Detail_View.as_view(), name="question-detail"),
    path('questions/<int:pk>/update/', views.Question_Update_View.as_view(), name="question-update"),
    path('questions/<int:pk>/delete/', views.Question_Delete_View.as_view(), name="question-delete"),
    path('questions/<int:pk>/comment/', views.Question_Comment_View.as_view(), name="question-comment"),
    path('questions/<int:pk>/<str:tag_name>/',views.Question_List_By_Tag_View.as_view(),name="question-tag"),
    path('tags/<str:tag_name>/',views.Question_List_By_Tag_View.as_view(),name="tag-question"),
    path('tags/', views.Tag_List_View.as_view(), name='tag-list'),
    path('like/<int:pk>', views.comment_like, name="like_post")
]
