from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.views import APIView


# Create your views here.
@api_view(["GET", "POST"])
def books(request):
    return Response("list of the books", status=status.HTTP_200_OK)


class BookList(APIView):
    def get(self, request):
        author = request.GET.get("author")
        if author:
            return Response(
                {"message": f"list of books by: {author}"}, status.HTTP_200_OK
            )
        return Response({"message": "list of the books"}, status.HTTP_200_OK)

    def post(self, request):
        return Response({"title": request.data.get("title")}, status.HTTP_201_CREATED)


class Book(APIView):
    def get(self, request, pk):
        return Response({"message": f"single book with id {pk}"}, status.HTTP_200_OK)

    def put(self, request, pk):
        return Response({"title": request.data.get("title")}, status.HTTP_200_OK)
