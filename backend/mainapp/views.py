from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import LeadershipTeam, AgeGroup, DiscipleshipGroup, RopesClass, ServingTeam, MinistryData
from .serializers import LeadershipTeamSerializer, AgeGroupSerializer,DiscipleshipGroupSerializer,RopesClassSerializer,ServingTeamSerializer,MinistryDataSerializer
from communication.models import Post
# Create your views here.

def is_pastor(user):
    return user.groups.filter(name='Pastors').exists()

def index(request):
    return render(request, 'index.html')

@login_required
@user_passes_test(is_pastor, login_url="/not-authorized/")
def pastors(request):
    return render(request, 'pastor.html')

@login_required
@user_passes_test(is_pastor, login_url="/not-authorized/")
def general(request):
    posts = Post.objects.all()[:3]
    context = {'posts': posts}
    return render(request, 'dashboards/pastors/general.html', context)

def not_authorized(request):
    return render(request, 'unauthorized.html')

@login_required
def home(request):
    return render(request, 'home.html')

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
    
    
class AgeGroupView(APIView):

    def get(self, request, *args, **kwargs):
        result = AgeGroup.objects.all()
        serializers = AgeGroupSerializer(result, many=True)
        return Response({'status': 'success', "age group": serializers.data}, status=200)
    
    def post(self, request):
        serializer = AgeGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, *args, **kwargs):
        try:
            group = AgeGroup.objects.get(id=kwargs['id'])
        except AgeGroup.DoesNotExist:
            return Response({"status": "error", "data": "Age Group not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AgeGroupSerializer(group, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, *args, **kwargs):
        try:
            group = AgeGroup.objects.get(id=kwargs['id'])
        except AgeGroup.DoesNotExist:
            return Response({"status": "error", "data": "group not found"}, status=status.HTTP_404_NOT_FOUND)
        
        group.delete()
        return Response({"status": "success", "data": "group deleted"}, status=status.HTTP_200_OK)
    

class DiscipleshipGroupView(APIView):

    def get(self, request, *args, **kwargs):
        result = DiscipleshipGroup.objects.all()
        serializers = DiscipleshipGroupSerializer(result, many=True)
        return Response({'status': 'success', "discipleship group": serializers.data}, status=200)
    
    def post(self, request):
        serializer = DiscipleshipGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, *args, **kwargs):
        try:
            group = DiscipleshipGroup.objects.get(id=kwargs['id'])
        except DiscipleshipGroup.DoesNotExist:
            return Response({"status": "error", "data": "Discipleship Group not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DiscipleshipGroupSerializer(group, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, *args, **kwargs):
        try:
            group = DiscipleshipGroup.objects.get(id=kwargs['id'])
        except DiscipleshipGroup.DoesNotExist:
            return Response({"status": "error", "data": "group not found"}, status=status.HTTP_404_NOT_FOUND)
        
        group.delete()
        return Response({"status": "success", "data": "group deleted"}, status=status.HTTP_200_OK)
    

class RopesClassView(APIView):

    def get(self, request, *args, **kwargs):
        result = RopesClass.objects.all()
        serializers = RopesClassSerializer(result, many=True)
        return Response({'status': 'success', "class": serializers.data}, status=200)
    
    def post(self, request):
        serializer = RopesClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, *args, **kwargs):
        try:
            ropes_class = RopesClass.objects.get(id=kwargs['id'])
        except RopesClass.DoesNotExist:
            return Response({"status": "error", "data": "ropes class not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = RopesClassSerializer(ropes_class, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, *args, **kwargs):
        try:
            ropes_class = RopesClass.objects.get(id=kwargs['id'])
        except RopesClass.DoesNotExist:
            return Response({"status": "error", "data": "ropes_class not found"}, status=status.HTTP_404_NOT_FOUND)
        
        ropes_class.delete()
        return Response({"status": "success", "data": "ropes_class deleted"}, status=status.HTTP_200_OK)
    
    
class ServingTeamView(APIView):

    def get(self, request, *args, **kwargs):
        result = ServingTeam.objects.all()
        serializers = ServingTeamSerializer(result, many=True)
        return Response({'status': 'success', "team": serializers.data}, status=200)
    
    def post(self, request):
        serializer = ServingTeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, *args, **kwargs):
        try:
            team = ServingTeam.objects.get(id=kwargs['id'])
        except ServingTeam.DoesNotExist:
            return Response({"status": "error", "data": "ropes class not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ServingTeamSerializer(team, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, *args, **kwargs):
        try:
            team = ServingTeam.objects.get(id=kwargs['id'])
        except ServingTeam.DoesNotExist:
            return Response({"status": "error", "data": "team not found"}, status=status.HTTP_404_NOT_FOUND)
        
        team.delete()
        return Response({"status": "success", "data": "team deleted"}, status=status.HTTP_200_OK)
    
    
class MinistryDataView(APIView):

    def get(self, request, *args, **kwargs):
        result = MinistryData.objects.all()
        serializers = MinistryDataSerializer(result, many=True)
        return Response({'status': 'success', "data": serializers.data}, status=200)
    
    def post(self, request):
        serializer = MinistryDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, *args, **kwargs):
        try:
            data = MinistryData.objects.get(id=kwargs['id'])
        except MinistryData.DoesNotExist:
            return Response({"status": "error", "data": "ropes class not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MinistryDataSerializer(data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, *args, **kwargs):
        try:
            data = MinistryData.objects.get(id=kwargs['id'])
        except MinistryData.DoesNotExist:
            return Response({"status": "error", "data": "data not found"}, status=status.HTTP_404_NOT_FOUND)
        
        data.delete()
        return Response({"status": "success", "data": "data deleted"}, status=status.HTTP_200_OK)
    
    
class LeadershipTeamViewSet(viewsets.ModelViewSet):
    queryset = LeadershipTeam.objects.all().order_by('id')
    serializer_class = LeadershipTeamSerializer

class AgeGroupViewSet(viewsets.ModelViewSet):
    queryset = AgeGroup.objects.all().order_by('id')
    serializer_class = AgeGroupSerializer

class DiscipleshipGroupViewSet(viewsets.ModelViewSet):
    queryset = DiscipleshipGroup.objects.all().order_by('id')
    serializer_class = DiscipleshipGroupSerializer

class RopesClassViewSet(viewsets.ModelViewSet):
    queryset = RopesClass.objects.all().order_by('id')
    serializer_class = RopesClassSerializer

class ServingTeamViewSet(viewsets.ModelViewSet):
    queryset = ServingTeam.objects.all().order_by('id')
    serializer_class = ServingTeamSerializer

class MinistryDataViewSet(viewsets.ModelViewSet):
    queryset = MinistryData.objects.all().order_by('id')
    serializer_class = MinistryDataSerializer
