from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import movies
from .serializers import moviesSerializers 

# Create your views here.


@api_view(['GET'])
def movieData(request):

    movie = movies.objects.all()

    serializer = moviesSerializers(movie, many = True)

    return Response(serializer.data)


@api_view(['POST'])
def movieCreate(request):

    serializer = moviesSerializers(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def movieUpdate(request, pk):

    movie = movies.objects.get(id = pk)
    
    serializer = moviesSerializers(instance = movie, data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def movieDelete(request, pk):

    movie = movies.objects.get(id = pk)

    movie.delete()

    return Response(f"Item with id {pk} was Deleted")