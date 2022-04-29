import datetime

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from reviews.models import Genre, Title, Category
from reviews.models import GenreTitle


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = 'name', 'slug'
        model = Genre


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = 'name', 'slug'
        model = Category


class TitleSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, required=False)
    category = CategorySerializer(required=True)

    def create(self, validated_data):
        if 'genre' not in self.initial_data:
            title = Title.objects.create(**validated_data)
            return title
        genres = validated_data.pop('genre')
        category = validated_data.pop('category')
        title = Title.objects.create(**validated_data)
        for genre in genres:
            current_genre, status = Genre.objects.get_or_create(
                **genre)
            GenreTitle.objects.create(
                genre_id=current_genre, title_id=title)
        Category.objects.get_or_create(
            **category
        )
        return title

    def validate_year(self, year):
        if (1000 > year
                or year > datetime.datetime.now().year):
            raise serializers.ValidationError('Некорректно введен год')
        return year

    class Meta:
        fields = ['id', 'name', 'year', 'category', 'genre']
        model = Title
        validators = [
            UniqueTogetherValidator(
                queryset=Title.objects.all(),
                fields=('name', 'year')
            )
        ]
