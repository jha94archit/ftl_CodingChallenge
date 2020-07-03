from django.db import models


class Member(models.Model):
    """ Custom User Model"""
    id = models.CharField(primary_key=True, editable=False, max_length=6)
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=255)


class ActivityPeriods(models.Model):
    #  Activity period model for user activity date and time
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='activity_periods')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


