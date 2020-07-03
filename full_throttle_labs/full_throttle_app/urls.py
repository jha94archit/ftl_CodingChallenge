from django.urls import path
from . import views

app_name = 'full_throttle_app'

urlpatterns = [
    path('api/member_activity/', views.MemberActivity.as_view(), name='member_activity'),
    path('api/activity/', views.ActivityView.as_view(), name='activity'),
]
