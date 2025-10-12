from rest_framework import serializers
from django.db.models import Avg
from movies.models import Movie
from genres.serializers import GenreSerializers
from actors.serializers import ActorSerializers


class MovieSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'

    def validade_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990')
        return value

    def validade_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('Resumo nao pode ter mais de 200 caracteres')


class MovieListDetailSerializers(serializers.ModelSerializer):
    actors = ActorSerializers(many=True)
    genre = GenreSerializers()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_data', 'rate', 'resume']

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(avg=Avg('stars'))['avg']

        if rate:
            return round(rate, 1)

        return None
