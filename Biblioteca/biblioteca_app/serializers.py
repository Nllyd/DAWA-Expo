from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_date', 'image_url']  # Incluye el nuevo campo

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), source='author')

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_date', 'author', 'author_id', 'image_url']  # Incluye el nuevo campo
