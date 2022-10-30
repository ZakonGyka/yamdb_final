from api.models import Category, Comments, Genre, Review, Title
from django.shortcuts import get_object_or_404
from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        exclude = ('title',)
        model = Review

    def validate(self, attrs):

        if self.context['request'].method != 'POST':
            return attrs
        title = get_object_or_404(
            Title,
            pk=self.context['view'].kwargs.get('title_id')
        )
        author = self.context['request'].user
        if Review.objects.filter(title=title, author=author).exists():
            raise serializers.ValidationError(
                'Нельзя публиковать больше одного отзыва на тайтл'
            )
        return attrs


class CommentsSerializer(serializers.ModelSerializer):

    review = serializers.SlugRelatedField(
        slug_field='text',
        read_only=True
    )

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Comments


class CategoryField(serializers.SlugRelatedField):
    def to_representation(self, value):
        serializer = CategorySerializer(value)
        return serializer.data


class GenreField(serializers.SlugRelatedField):
    def to_representation(self, value):
        serializer = GenreSerializer(value)
        return serializer.data


class TitleSerializer(serializers.ModelSerializer):
    category = CategoryField(
        slug_field='slug',
        queryset=Category.objects.all(),
        required=False
    )
    genre = GenreField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True
    )
    rating = serializers.IntegerField(read_only=True, required=False)

    class Meta:
        fields = '__all__'
        model = Title


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('id',)
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('id',)
        model = Genre
