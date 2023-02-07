from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.db import IntegrityError
from .forms import AddBookForm
from .models import BookListModel, Book
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Create your views here.
@csrf_exempt
def add(request):
    form = AddBookForm()
    if request.method == "POST":
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'new_book':form}
    print(context)
    return JsonResponse({'status':"success"},safe=False)
# def books(request):
#     books = BookListModel.objects.all().values()
   
#     return JsonResponse(list(books),safe=False)
# @api_view()
# def books(request):
    if request.method == 'GET':
        books = Book.objects.all().values()
        return Response(books, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        book = Book(
            title = title,
            author = author,
            price = price
        )
        try:
            book.save()
        except IntegrityError:
            return JsonResponse({'error':'true','message':'required field missing'},status=400)

        return Response(book, status=status.HTTP_300_OK)

@api_view(['post','GET'])
def books2(request):
    return Response('List of the books',status=status.HTTP_200_OK)

class BookList(APIView):
    def get(self, request):
        author = request.GET.get('author')
        if author:
            return Response({'message':"All author books find and author name "+author},status.HTTP_200_OK)
        return Response({'message':"this is the list class base view"},status.HTTP_200_OK)
    

class Book(APIView):
    def get(self,request,pk):
        return Response({'message':"Get the book with primary key "+ str(pk)},status.HTTP_200_OK)
    def put(self,request,pk):
        return Response({"message":"my name updated, name = "+ request.data.get('name')},status.HTTP_200_OK)
