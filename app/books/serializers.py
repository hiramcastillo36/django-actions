from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    published = serializers.DateField()

    class Meta:
        model = Book
        fields = '__all__'
