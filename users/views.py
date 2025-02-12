from rest_framework import generics, permissions
from .models import CustomUser, Profile
from .serializers import UserRegisterSerializer, ProfileSerializer


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer


class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all().order_by('-id')
    serializer_class = ProfileSerializer

class ProfileDetailView(generics.RetrieveUpdateAPIView):  # PUT va GET uchun
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
