from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from ..models import Makale, Gazeteci
from .serializers import MakaleSerializer, GazeteSerializer


class YazarlarListApiView(APIView):

    def get(self, request):
        yazarlar = Gazeteci.objects.all()
        serializer = GazeteSerializer(
            yazarlar, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = GazeteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class YazarDetailApiView(APIView):

    def get_object(self, pk):
        yazar_instance = get_object_or_404(Gazeteci, pk=pk)
        return yazar_instance

    def get(self, request, pk):
        yazar = self.get_object(pk=pk)
        serializer = GazeteSerializer(yazar, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        yazar = self.get_object(pk=pk)
        serializer = GazeteSerializer(
            yazar, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        yazar = self.get_object(pk=pk)
        yazar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MakaleListApiView(APIView):

    def get(self, request):
        makaleler = Makale.objects.filter(aktif=True)
        serializer = MakaleSerializer(makaleler, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MakaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MakaleDetailApiView(APIView):

    def get_object(self, pk):
        makale_instance = get_object_or_404(Makale, pk=pk)
        return makale_instance

    def get(self, request, pk):
        makale = self.get_object(pk=pk)
        serializer = MakaleSerializer(makale)
        return Response(serializer.data)

    def put(self, request, pk):
        makale = self.get_object(pk=pk)
        serializer = MakaleSerializer(makale, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        makale = self.get_object(pk=pk)
        makale.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


""" @api_view(['GET', 'POST'])
def makale_list_api_view(request):

    if request.method == 'GET':
        makaleler = Makale.objects.filter(aktif=True)
        serializer = MakaleSerializer(makaleler, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MakaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
 """


""" @api_view(['GET', 'PUT', 'DELETE'])
def makale_detail(request, pk):
    try:
        makale_instance = Makale.objects.get(pk=pk)
    except:
        return Response({
            'errors': {'code': 404,
                        'message': 'BÖyle bir makale Yoktur'

                        }
        }, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MakaleSerializer(makale_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MakaleSerializer(makale_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        makale_instance.delete()
        return Response({'Cevap': {
            'code': 204,
            'message': f'{pk} id numaralı makale silindi'
        }}, status=status.HTTP_204_NO_CONTENT)
 """
