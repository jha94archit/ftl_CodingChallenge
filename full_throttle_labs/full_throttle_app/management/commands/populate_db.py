""" populate_db management command to populate db with dummy data"""
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from core.models import Member, ActivityPeriods
from faker import Faker
import datetime
import string
import random


def gen_id():
    """Id generator method to generate required id"""
    res = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=7))
    random_id = 'W0' + str(res)
    return random_id


class Command(BaseCommand):
    """Create management command populate_db"""
    help = 'Create N random users where N is the number of users.'

    def add_arguments(self, parser):
        """Accept number argument to populate that count of records"""
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        """Handler for on command execution"""
        total = kwargs['total']
        fake = Faker()
        records_user = []
        records_activity = []
        """Create member records"""
        for i in range(total):
            member_id = gen_id()
            user_detail = {
                'id': member_id,
                'real_name': fake.name(),
                'tz': fake.timezone()
            }
            record = Member(**user_detail)
            records_user.append(record)
        Member.objects.bulk_create(records_user)
        print("User Records Creation -- Success")
        queryset = Member.objects.all()
        """Create activity period records"""
        for user_obj in queryset:
            for i in range(total):
                st = fake.date_time_this_year()
                et = st + datetime.timedelta(hours=random.randint(3, 6))
                activity_detail = {
                    'member_id': user_obj,
                    'start_time': make_aware(st),
                    'end_time': make_aware(et)
                }
                activity_record = ActivityPeriods(**activity_detail)
                records_activity.append(activity_record)
        ActivityPeriods.objects.bulk_create(records_activity)
        print("User Activity Records Creation -- Success")
