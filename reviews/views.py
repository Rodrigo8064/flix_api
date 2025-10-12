from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from reviews.models import Review
from reviews.serializers import ReviewSerializers, ReviewListDetailSerializer
from app.permissions import GlobalPermission


class ReviewCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermission,)
    queryset = Review.objects.all()
  
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReviewListDetailSerializer
        return ReviewSerializers


class ReviewRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermission,)
    queryset = Review.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReviewListDetailSerializer
        return ReviewSerializers
