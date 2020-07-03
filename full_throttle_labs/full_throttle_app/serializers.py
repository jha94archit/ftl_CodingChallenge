from rest_framework import serializers, fields
from core.models import Member, ActivityPeriods


class ActivityPeriodsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityPeriods
        fields = ['start_time', 'end_time']


class MemberSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodsSerializer(read_only=True, many=True)

    class Meta:
        model = Member
        fields = ['id', 'real_name', 'tz', 'activity_periods']


