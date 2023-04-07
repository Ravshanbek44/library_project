from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializes
from rest_framework import generics, status, viewsets


# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializes
class BookListApiView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializes(books, many=True).data
        data = {
            'status': f"Returned {len(books)} books",
            'books': serializer_data
        }
        return Response(data)

# class BookDetailApiview(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializes
class BookDetailApiview(APIView):

    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSerializes(book).data
            data = {
                'status': "successful",
                'book': serializer_data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {'status': False,
                 "message": "Book is not found"}, status=status.HTTP_404_NOT_FOUND
            )

# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializes
class BookDeleteApiView(APIView):

    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return Response({
                'status': "True",
                'message': "successfuly deleted"
            }, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                'status': "False",
                'message': "book is not found"
            }, status=status.HTTP_400_BAD_REQUEST)

# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializes
class BookUpdateApiView(APIView):

    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serializer = BookSerializes(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response(
            {
                "status": True,
                'message': f"book{book.save} updated successfully"
            }
        )

# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializes
class BookCreateApiView(APIView):

    def post(self, request):
        data = request.data
        serializer = BookSerializes(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {
                'status': f"books are saved to database",
                'books': data
            }
            return Response(data)

class BookListCreatApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializes

class BookUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializes


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializes



