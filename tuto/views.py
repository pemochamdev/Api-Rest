from django.contrib.auth.models import User, Group
from django.shortcuts import render


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


from tuto.serializers import UserSrializer, GroupSerializer

class UserViewSet(ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSrializer
    permission_classes = [IsAuthenticated]



class GroupViewSet(ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]
    
