from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('authors', views.authors, name='authors'),
    path('authors/<int:pk>', views.AutorDetailView.as_view(),
         name='author_detail'),
    path('books/', views.KnihaListView.as_view(), name='books_list'),
    path('books/<int:pk>', views.KnihaDetailView.as_view(),
         name='book_detail'),
    path('books/genres/<int:id>', views.knihy_podle_zanru,
         name='books_by_genre'),
    path('books/add', views.KnihaCreateView.as_view(), name='add_book'),
    path('books/update/<int:pk>', views.KnihaUpdateView.as_view(), name='update_book'),
    path('books/delete/<int:pk>', views.KnihaDeleteView.as_view(), name='delete_book'),
    path('authors/add', views.AutorCreateView.as_view(), name='add_autor'),
    path('authors/update/<int:pk>', views.AutorUpdateView.as_view(), name='update_autor'),
    path('authors/delete/<int:pk>', views.AutorDeleteView.as_view(), name='delete_autor'),
]
