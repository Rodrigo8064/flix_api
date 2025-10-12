from rest_framework import serializers
from reviews.models import Review
from movies.serializers import MovieListDetailSerializers


class ReviewSerializers(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


class ReviewListDetailSerializer(serializers.ModelSerializer):
    movie = MovieListDetailSerializers()

    class Meta:
        model = Review
        fields = ['id', 'movie', 'stars', 'comment']
