import datetime

from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.validators import UniqueTogetherValidator
from reviews.models import Category, Genre, GenreTitle, Review, Title


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
        category_slug = validated_data.pop('category')
        category = get_object_or_404(Category, slug=category_slug)
        if 'genre' not in self.initial_data:
            title = Title.objects.create(**validated_data, category=category)
            return title
        genres = validated_data.pop('genre')
        print(genres)

        title = Title.objects.create(**validated_data)
        for genre_slug in genres:
            current_genre = get_object_or_404(Genre, slug=genre_slug)
            GenreTitle.objects.create(
                genre=current_genre, title=title)
        title.save(category=category)
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


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    pub_date = serializers.DateTimeField(
        read_only=True,
        source='pub_date'
    )

    class Meta:
        fields = '__all__'
        model = Review
