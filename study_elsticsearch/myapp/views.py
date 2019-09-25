from django.shortcuts import render

# Create your views here.
from drf_haystack.viewsets import HaystackViewSet
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from myapp.models import Book
from myapp.serizlizers import BookIndexSerializer, BookSerializer

class MyPageNumberPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'
    page_size_query_param="size"
    # max_page_size=10
class BookSearchViewSet(HaystackViewSet):
    """
    SKU搜索
    """
    index_models = [Book]
    serializer_class = BookIndexSerializer
    pagination_class = MyPageNumberPagination
    def list(self, request, *args, **kwargs):
        bookname=self.request.query_params.get('bookname')
        print(bookname,'bookname')
        queryset = self.filter_queryset(self.get_queryset())
        # queryset = queryset.filter()#想实现条件搜索在search_indexes.py文件里，一定要重新创建索引
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class BookAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer