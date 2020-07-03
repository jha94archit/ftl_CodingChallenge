from core.models import Member, ActivityPeriods
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from rest_framework import generics
import json


class MemberActivityView(APIView):
    """ View to check if data in db and list member and activity details """
    def get(self, request):
        queryset = Member.objects.all()                                 # Fetch all Member Objects in DB
        if queryset:                                                    # Check if data present in DB
            serializer_class = MemberSerializer(queryset, many=True)    # Invoke serializer with member objects
            # many=True because handling nested multiple records
            member_activity_data = serializer_class.data                # Retrieve data from serializer
            content = {
                "ok": True,                                             # Show DB has data
                "members": member_activity_data                         # Member data
            }
            json.dumps(content)                                         # Creates nested JSON
            return Response(content)                                    # Response with JSON to api call
        else:
            return Response({
                "ok": False                                             # Show DB is empty
            })

