from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import LeadershipTeam, AgeGroup, DiscipleshipGroup, RopesClass, ServingTeam, MinistryData
from .serializers import LeadershipTeamSerializer, AgeGroupSerializer,DiscipleshipGroupSerializer,RopesClassSerializer,ServingTeamSerializer,MinistryDataSerializer
# Create your views here.
def index(request):
    return render(request, 'index.html')

class LeadershipTeamView(APIView):

    def get(self, request, *args, **kwargs):
        result = LeadershipTeam.objects.all()
        serializers = LeadershipTeamSerializer(result, many=True)
        return Response({'status': 'success', "leadership team": serializers.data}, status=200)
    
    def post(self, request):
        serializer = LeadershipTeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, *args, **kwargs):
        try:
            team = LeadershipTeam.objects.get(id=kwargs['id'])
        except LeadershipTeam.DoesNotExist:
            return Response({"status": "error", "data": "Team not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = LeadershipTeamSerializer(team, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, *args, **kwargs):
        try:
            team = LeadershipTeam.objects.get(id=kwargs['id'])
        except LeadershipTeam.DoesNotExist:
            return Response({"status": "error", "data": "team not found"}, status=status.HTTP_404_NOT_FOUND)
        
        team.delete()
        return Response({"status": "success", "data": "team deleted"}, status=status.HTTP_200_OK)
    
    