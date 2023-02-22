from django.shortcuts import render

from django.db import models
from rest_framework.response import Response 
from rest_framework import viewsets 
from .models import MenuItem 
from .serializers import MenuItemSerializer
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from .throttles import TenCallsPerMinute

class MenuItemsViewSet(viewsets.ModelViewSet):
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    throttle_classes = [TenCallsPerMinute]
    def get_throttles(self):
        if self.action == 'create':
            throttle_classes = [UserRateThrottle]
        else:
            throttle_classes = []
        return [throttle() for throttle in throttle_classes]


