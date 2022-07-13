from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Makale
from .serializers import MakaleSerializer


@api_view(['GET', 'POST'])
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
