from django.shortcuts import render
from rest_framework import viewsets
from .models import Server
from .serializer import ServerSerializer
from rest_framework.response import Response

# Create your views here.
class ServerListViewSet(viewsets.ViewSet):
    
    queryset = Server.objects.all()
    
    def list(self, request):
        category = request.query_params.get("category")
        result = self.queryset
        if category:
            result = result.filter(category__name=category)
            
        serializer = ServerSerializer(result, many=True)
        return Response(data=serializer.data)
        
        
        
