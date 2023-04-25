"""View module for handling requests about trips"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from househubapi.models import Home

class HomeView(ViewSet):
    """HouseHub Home view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single home

        Returns:
            Response -- JSON serialized home
        """
        try:
            home = Home.objects.get(pk=pk)
            serializer = HomeSerializer(home)
            return Response(serializer.data)
        except Home.DoesNotExist as ex:
            return Response({'message:': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all homes

        Returns:
            Response -- JSON serialized list of homes
        """
        home = Home.objects.all()

        filtering = request.query_params.get("filter_by", None)
        if filtering is not None and filtering == "user":
            home = home.filter(user=request.auth.user)

        serializer = HomeSerializer(home, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST requests to create a new home

        Returns:
            Response -- JSON serialized dictionary representation of the new home
        """
        serializer = CreateHomeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=request.auth.user
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk=None):
        """Handle PUT requests to update a home

        Returns:
            Response -- JSON serialized dictionary representation of the updated home
        """
        home = Home.objects.get(pk=pk)
        serializer = CreateHomeSerializer(home, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()       
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests to destroy a home

        Returns:
            Response: None with 204 status code
        """
        try:
            home = Home.objects.get(pk=pk)
            home.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Home.DoesNotExist:
            return Response({'message': 'You sent an invalid home'}, status=status.HTTP_404_NOT_FOUND)
        
class UserHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', "first_name", "last_name")

class CreateHomeSerializer(serializers.ModelSerializer):
    """JSON serializer for creating a trip
    """

    class Meta:
        model = Home
        fields = ('id', 'name', 'street', 'city', 'state', 
                  'country', 'bedrooms', 'bathrooms', 
                  'sq_footage', 'lot_size')
        depth = 1

class HomeSerializer(serializers.ModelSerializer):
    """JSON serializer for homes
    """
    user = UserHomeSerializer(many=False)

    class Meta:
        model = Home
        fields = ('id', 'name', 'street', 'city', 'state', 
                  'country', 'bedrooms', 'bathrooms', 
                  'sq_footage', 'lot_size', 'user')
        depth = 1