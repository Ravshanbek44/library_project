from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import BookListApiView,   BookDetailApiview, \
    BookDeleteApiView, BookUpdateApiView, BookCreateApiView, \
    BookListCreatApiView, BookUpdateDeleteApiView, BookViewSet

router =SimpleRouter()
router.register('books', BookViewSet, basename='books')

urlpatterns = [
    # path('books/', BookListApiView.as_view()),
    # path('booklistcreate/', BookListCreatApiView.as_view()),
    # path('bookupdatedelete/<int:pk>/', BookUpdateDeleteApiView.as_view()),
    # path('books/create/', BookCreateApiView.as_view()),
    # path('books/<int:pk>/', BookDetailApiview.as_view()),
    # path('books/<int:pk>/update/', BookUpdateApiView.as_view()),
    # path('books/<int:pk>/delete/', BookDeleteApiView.as_view()),
]

urlpatterns = urlpatterns+router.urls