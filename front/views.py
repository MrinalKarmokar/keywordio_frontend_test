import json

import requests
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index_view(request, *args, **kwargs):
    context = {

    }
    return render(request, 'library/index.html', context)

@csrf_exempt
def signup_view(request, *args, **kwargs):

    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')

        URL = 'http://127.0.0.1:8000/api/user/signup/'
        
        headers = {
            'content-type': 'application/json; charset=UTF-8',
        }

        body = {
            "email": email,
            "password": password,
            "password2": password2
        }

        response = requests.post(URL, data=json.dumps(body), headers=headers)
        json_response = response.json()
        token = json_response['token']

        res =  redirect('login')
        res.set_cookie('token', token)
        return res
    
    return render(request, 'accounts/signup.html')

@csrf_exempt
def login_view(request, *args, **kwargs):

    if request.method == 'POST':
        email = request.POST.get('username', '')
        password = request.POST.get('password', '')

        URL = 'http://127.0.0.1:8000/api/user/login/'

        token = request.COOKIES.get('token')
        access_token = token[1]

        headers = {
            'content-type': 'application/json; charset=UTF-8',
            'Authorization': f'Bearer {access_token}'
        }

        body = {
            "email": email,
            "password": password
        }

        response = requests.post(URL, data=json.dumps(body), headers=headers)
        json_response = response.json()

        res =  redirect('index')
        res.set_cookie('token', token)
        return res
    
    if request.method == "GET":

        URL = "http://127.0.0.1:8000/api/token/refresh/"

        headers = {
            'content-type': 'application/json; charset=UTF-8',
        }

        token = request.COOKIES.get('token')
        refresh_token = token[0]
        body = {
            "refresh": refresh_token,
        }
        response = requests.post(URL, data=json.dumps(body), headers=headers)

    return render(request, 'accounts/login.html')


def logout_view(request):
    '''Logging Out Users and clearing sessions'''

    logout(request)
    return redirect('/')


def get_all_books_view(request):
        URL = "http://127.0.0.1:8000/api/library/get-book/"

        response = requests.get(URL)

        context = {
            "response": response.json()
        }

        return render(request, 'library/get_all_books.html', context)

def update_books_view(request):
    URL = ""
    pass


def add_books_view(request):
    URL = "http://127.0.0.1:8000/api/library/add-book/"

    if request.method == 'POST':
        title = request.POST.get('title', '')
        author = request.POST.get('author', '')
        num_pages = request.POST.get('num_pages', '')
        publication = request.POST.get('publication', '')
        publisher = request.POST.get('publisher', '')

        URL = 'http://127.0.0.1:8000/api/user/signup/'
        
        token = request.COOKIES.get('token')
        access_token = token[1]

        headers = {
            'content-type': 'application/json; charset=UTF-8',
            'Authorization': f'Bearer {access_token}'
        }

        body = {
            "title": title,
            "author": author,
            "num_pages": num_pages,
            "publication": publication,
            "publisher": publisher,
        }

        response = requests.post(URL, data=json.dumps(body), headers=headers)

        print(response.json())
    
        return render(request, 'library/add_books.html')

    if request.method == "GET":

        URL = "http://127.0.0.1:8000/api/token/refresh/"

        headers = {
            'content-type': 'application/json; charset=UTF-8',
        }

        token = request.COOKIES.get('token')
        refresh_token = token[1]
        body = {
            "refresh": refresh_token,
        }
        response = requests.post(URL, data=json.dumps(body), headers=headers)

        return render(request, 'library/add_books.html')

