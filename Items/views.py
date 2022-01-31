from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework import generics,mixins
from .models import Item
from .serializers import ItemSerializer
from django.http import Http404


# Create your views here.
def get_object(pk):
    try:
        return Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        raise Http404


class ItemCreateView(generics.CreateAPIView, mixins.CreateModelMixin):
    serializer_class = ItemSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class ItemView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        qs = Item.objects.all().order_by("-timestamp")
        serializer = ItemSerializer(qs, many=True)
        return Response(serializer.data)


class ItemDetailView(APIView):

    def get(self, request, pk, format=None):
        qs = get_object(pk)
        serializer = ItemSerializer(qs)
        return Response(serializer.data)


class ItemEdit(APIView):
    def put(self, request, pk, format=None):
        qs = get_object(pk)
        serializer = ItemSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemDelete(APIView):

    def delete(self, request, pk, format=None):
        qs = get_object(pk)
        qs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)