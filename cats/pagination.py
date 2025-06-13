from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CatPagination(PageNumberPagination):
    page_size = 20

    def get_paginated_response(self, data):
        return Response({'response': data})