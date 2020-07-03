from core.models import Member, ActivityPeriods
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from rest_framework import generics
import json


class MemberActivityView(APIView):
    """ View to check if data in db and list member and activity details """
    def get(self, request):
        queryset = Member.objects.all()
        if queryset:
            serializer_class = MemberSerializer(queryset, many=True)
            member_activity_data = serializer_class.data
            content = {
                "ok": True,
                "members": member_activity_data
            }
            json.dumps(content)
            return Response(content)
        else:
            return Response({
                "ok": False
            })

