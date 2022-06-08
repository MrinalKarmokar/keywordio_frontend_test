from django.urls import path, include
from front.views import *

urlpatterns = [
    path('login/', login_view, name="login"),
    path('signup/', signup_view, name="signup"),
    path('logout/', logout_view, name="logout"),
    path('get-books/', get_all_books_view, name="get_all_books"),
    # path('update-books/', update_books_view, name="update_view"),
    path('add-books/', add_books_view, name="add_view"),
    path('', index_view, name="index"),
]
