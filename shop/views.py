# _*_ coding:utf-8 _*_
from django.http import HttpResponse
from django.shortcuts import render
from django.template.context import RequestContext


from models import User, Book

from django import forms
from django.forms import ModelForm

class UserForm(forms.Form):
        name = forms.CharField(max_length=30 ,label='用户名')
        age = forms.IntegerField(label='年龄')
        sex = forms.ChoiceField(choices=[('1',u'男'),('2',u'女')])
        books = forms.CharField(max_length=30 ,label='书籍')
class UsersForm(ModelForm):
        class Meta:
                model = User
                fields = ('name','age','sex','books')
                labels={
                    'name':"姓名",
                    'age':'年龄',
                    'sex': '性别',
                    'books':'书籍'
                    }
class BookForm(forms.Form):
        name = forms.CharField(max_length=30 ,label='书名')
        price = forms.FloatField(label='价格')
        users = forms.CharField(max_length=30 ,label='作者')

class BooksForm(ModelForm):
        class Meta:
                model = Book
                fields = ('name','price', 'users')
                labels={
                    'name':"书名",
                    'price':'价格',
                    'users': '作者'
                    }


def index(request):
    users = User.objects.all()
    books = Book.objects.all()
    return render(request, 'index.html', {'users':users,'books':books})

def user(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            age = form.cleaned_data["age"]
            sex = form.cleaned_data["sex"]
            books = form.cleaned_data["books"]
            if not User.objects.filter(name=name).first():
                User.objects.create(name=name,age=age,sex=sex)
                if User.objects.filter(name=name).first():
                    obj = User.objects.filter(name=name).first()
                    a = [i.id for i in books]
                    obj.books.add(*a)
            else:
                return HttpResponse("创建失败")
    form = UsersForm()
    users = User.objects.all()
    return render(request, 'user.html', {'form':form, 'users':users})
    
def book(request):
    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            price = form.cleaned_data["price"]
            users = form.cleaned_data["users"]
            if not Book.objects.filter(name=name).first():
                Book.objects.create(name=name,price=price)
                if Book.objects.filter(name=name).first():
                    obj = Book.objects.filter(name=name).first()
                    a = [i.id for i in users]
                    obj.users.add(*a)
            else:
                return HttpResponse("创建失败")
    form = BooksForm()
    books = Book.objects.all()
    return render(request, 'book.html', {'form':form, 'books':books})
