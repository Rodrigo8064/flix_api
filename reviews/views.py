from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from reviews.models import Review
from reviews.serializers import ReviewSerializers
from app.permissions import GlobalPermission


class ReviewCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermission,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers


class ReviewRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermission,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
