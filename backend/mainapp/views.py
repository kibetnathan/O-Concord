from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import LeadershipTeam, AgeGroup, DiscipleshipGroup, RopesClass, ServingTeam, MinistryData
from .serializers import LeadershipTeamSerializer, AgeGroupSerializer,DiscipleshipGroupSerializer,RopesClassSerializer,ServingTeamSerializer,MinistryDataSerializer
# Create your views here.
def index(request):
    return render(request, 'index.html')
