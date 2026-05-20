from django.urls import path

from .views import (
    RegisterView,
    ChangePasswordView,
    BookListCreateView,
    BookDetailView,
    BookReviewListCreateView,
    ReviewDetailView
)

urlpatterns = [

    # Authentication
    path('register/', RegisterView.as_view(), name='register'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),

    # Books
    path('books/', BookListCreateView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Reviews
    path(
        'books/<int:book_id>/reviews/',
        BookReviewListCreateView.as_view(),
        name='book-reviews'
    ),

    path(
        'reviews/<int:pk>/',
        ReviewDetailView.as_view(),
        name='review-detail'
    ),
]