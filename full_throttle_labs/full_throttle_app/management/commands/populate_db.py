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
                                 string.digits, k=7))                   # Generate random string
    random_id = 'W0' + str(res)
    return random_id                                                    # Return generated id


class Command(BaseCommand):
    """Create management command populate_db"""
    help = 'Create N random users where N is the number of users.'      # Help info for management command

    def add_arguments(self, parser):
        """Accept number argument to populate that count of records"""
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        """Handler for on command execution"""
        total = kwargs['total']                         # Accept integer from command argument
        fake = Faker()                                  # Initialize faker instance
        records_user = []                               # List to append member info to create bulk record in DB
        records_activity = []                           # List to append activity_info info to create bulk record in DB
        """Create member records"""
        for i in range(total):                          # Loop till value passed to create that many records
            member_id = gen_id()                        # call gen_id() method to generate member id
            user_detail = {
                'id': member_id,
                'real_name': fake.name(),               # Create fake name using Faker package
                'tz': fake.timezone()                   # Create fake timezone using Faker package
            }
            record = Member(**user_detail)              # Creating record instance with complete member details
            records_user.append(record)                 # Append in the list for bulk creation
        Member.objects.bulk_create(records_user)        # Using list to bulk create members
        print("User Records Creation -- Success")
        queryset = Member.objects.all()                 # Fetch all members in the DB
        """Create activity period records"""
        for user_obj in queryset:                       # Loop to iterate through each object
            for i in range(total):                      # Loop to iterate passed arguments time
                st = fake.date_time_this_year()         # Generate fake start time using Faker
                et = st + datetime.timedelta(hours=random.randint(3, 6))
                # To ensure end time is after start time adding random hours ranging from 3-6 to start time
                activity_detail = {                     # Create activity_detail object with st and et
                    'member_id': user_obj,
                    'start_time': make_aware(st),       # make_aware() used to incorporate server-timezone
                    'end_time': make_aware(et)
                }
                activity_record = ActivityPeriods(**activity_detail)
                # Creating record instance with complete member activity detail
                records_activity.append(activity_record)
                # Append in the list for bulk creation
        ActivityPeriods.objects.bulk_create(records_activity)
        print("User Activity Records Creation -- Success")
        # Using list to bulk create members
