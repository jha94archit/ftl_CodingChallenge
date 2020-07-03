from django.db import models


class Member(models.Model):
    """ Custom User Model"""
    id = models.CharField(primary_key=True, editable=False, max_length=6)       # Member ID
    real_name = models.CharField(max_length=100)                                # Member real name
    tz = models.CharField(max_length=255)                                       # Timezone of member


class ActivityPeriods(models.Model):
    """Activity period model for user activity date and time"""

    member_id = models.ForeignKey(Member, on_delete=models.CASCADE,
                related_name='activity_periods')              # Member ID Foreign Key reference to member model
    start_time = models.DateTimeField()                                         # Member activity start time
    end_time = models.DateTimeField()                                           # Member activity end time


