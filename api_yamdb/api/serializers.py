import datetime
from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.validators import UniqueTogetherValidator

from reviews.models import Genre, Title, Category, User, GenreTitle


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


class RegistrationSerializer(serializers.ModelSerializer):
    confirmation_code = serializers.CharField(max_length=64, read_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = (
            'username', 'email', 'confirmation_code', 'token'
        )

    def validate_username(self, username):
        if username == 'me':
            raise serializers.ValidationError(
                'Сочетание "me" нельзя использовать в качестве никнейма.'
            )
        return username

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.email_user(
            subject='confirmation_code',
            message=user.confirmation_code
        )
        return {
            'email': user.email,
            'username': user.username,
        }


class LoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = (
            'username', 'confirmation_code', 'token'
        )

    def validate(self, data):
        username = data.get('username', None)
        code = data.get('confirmation_code', None)

        user = get_object_or_404(
            User,
            username=username,
            confirmation_code=code
        )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return {
            'token': user.token
        }
