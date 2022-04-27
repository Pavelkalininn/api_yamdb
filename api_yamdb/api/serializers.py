import datetime

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from reviews.models import Genre, Title, Category


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Genre


class TitleSerializer(serializers.ModelSerializer):

    def validate_year(self, data):
        if (1000 > data['year']
                or data['year'] > datetime.datetime.now().year.__str__()):
            raise serializers.ValidationError(
                'Неорректно введен год')
        return data

    class Meta:
        fields = '__all__'
        model = Title
        validators = [
            UniqueTogetherValidator(
                queryset=Title.objects.all(),
                fields=('model', 'year')
            )
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category

