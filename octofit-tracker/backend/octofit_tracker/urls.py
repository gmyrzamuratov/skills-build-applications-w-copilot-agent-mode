from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.api_root, name='api-root'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<str:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('teams/', views.TeamList.as_view(), name='team-list'),
    path('teams/<str:pk>/', views.TeamDetail.as_view(), name='team-detail'),
    path('activity/', views.ActivityList.as_view(), name='activity-list'),
    path('activity/<str:pk>/', views.ActivityDetail.as_view(), name='activity-detail'),
    path('leaderboard/', views.LeaderboardList.as_view(), name='leaderboard-list'),
    path('leaderboard/<str:pk>/', views.LeaderboardDetail.as_view(), name='leaderboard-detail'),
    path('workouts/', views.WorkoutList.as_view(), name='workout-list'),
    path('workouts/<str:pk>/', views.WorkoutDetail.as_view(), name='workout-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
