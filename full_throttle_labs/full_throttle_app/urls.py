from django.urls import path
from . import views

app_name = 'full_throttle_app'

urlpatterns = [
    path('api/member_activity/', views.MemberActivityView.as_view(), name='member_activity'),
]
