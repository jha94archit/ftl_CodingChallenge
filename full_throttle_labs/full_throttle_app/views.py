from core.models import Member, ActivityPeriods
from .serializers import *
from rest_framework import generics


class MemberActivity(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class ActivityView(generics.ListAPIView):
    queryset = ActivityPeriods.objects.all()
    serializer_class = ActivityPeriodsSerializer