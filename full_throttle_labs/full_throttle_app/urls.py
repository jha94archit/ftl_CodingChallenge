from django.urls import path
from . import views

app_name = 'full_throttle_app'

urlpatterns = [
    path('api/member/', views.MemberActivity.as_view(), name='member'),
    path('api/activity/', views.ActivityView.as_view(), name='activity'),
    path('api/member_activity/', views.MemberActivityView.as_view(), name='member_activity'),
]
