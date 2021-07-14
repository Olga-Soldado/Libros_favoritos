from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    # List of books page
    path('books', views.books),
    # Add a new book
    path('add_book/<int:user_id>', views.add_book),
    # Profile of 1 book
    path('books/<int:book_id>', views.book_profile),
    # Edit a book
    path('edit_book/<int:book_id>', views.edit_book),
    # Delete a book
    path('delete_book/<int:book_id>', views.delete_book),
    # Unfavorite a book
    path('unfavorite/<int:book_id>/<int:user_id>', views.unfavorite),
    # Favorite a book
    path('add_to_favorites/<int:book_id>/<int:user_id>', views.add_to_favorites),
    # List of favorite books for the logged in user
    path('favorite_books', views.favorite_books),

]
