from drf_haystack.serializers import HaystackSerializer
from rest_framework import serializers

from myapp.models import Book
from myapp.search_indexes import BookIndex


class BookSerializer(serializers.ModelSerializer):
    """
    SKU索引结果数据序列化器
    """
    class Meta:
        model =Book
        fields = ( 'id', 'bookname', 'book_type','is_hot_sale', 'book_word_counts')

class BookIndexSerializer(HaystackSerializer):
    """
    SKU索引结果数据序列化器
    """
    object = BookSerializer(read_only=True)
    class Meta:
        index_classes = [BookIndex]
        fields = ( 'id', 'bookname', 'book_type')