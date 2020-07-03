from rest_framework import serializers, fields
from core.models import Member, ActivityPeriods


class ActivityPeriodsSerializer(serializers.ModelSerializer):
    """Serializer for member activity periods"""
    class Meta:
        model = ActivityPeriods
        fields = ['start_time', 'end_time']                 # Fields which have to be serialized and deserialized


class MemberSerializer(serializers.ModelSerializer):
    """ Serializer for Member details"""
    activity_periods = ActivityPeriodsSerializer(read_only=True, many=True)
    # Referencing ActivityPeriodSerializer to member serializer
    # For nested serializer to show activity period with related member
    # many=True because every member has multiple activity records

    class Meta:
        model = Member
        fields = ['id', 'real_name', 'tz', 'activity_periods']     # Fields which have to be serialized and deserialized


