from django.urls import path
from .views import CreateUserListView,UserDetailAPIView

urlpatterns = [
    path('user-create-list/',CreateUserListView.as_view(), name="create-user"),
    path('user-detail/<int:user_id>/', UserDetailAPIView.as_view(), name='user-detail'),
]