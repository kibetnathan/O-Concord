from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import CustomUser, Profile
from .serializers import UserSerializer, ProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid credentials"
    else:
        error_message = None
    return render(request, 'login.html', {'error_message': error_message})

class ProfileView(APIView):

    def get(self, request, *args, **kwargs):
        result = Profile.objects.all()
        serializers = ProfileSerializer(result, many=True)
        return Response({'status': 'success', "profile": serializers.data}, status=200)
    
    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, *args, **kwargs):
        try:
            profile = Profile.objects.get(id=kwargs['id'])
        except Profile.DoesNotExist:
            return Response({"status": "error", "data": "profile not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, *args, **kwargs):
        try:
            profile = Profile.objects.get(id=kwargs['id'])
        except Profile.DoesNotExist:
            return Response({"status": "error", "data": "profile not found"}, status=status.HTTP_404_NOT_FOUND)
        
        profile.delete()
        return Response({"status": "success", "data": "profile deleted"}, status=status.HTTP_200_OK)