from django.urls import path
from .views import CreateSnippet, ViewSnippet

urlpatterns = [
    path('create/', CreateSnippet.as_view(),  name='create_snippet'),
    path('create/view_snippet/', ViewSnippet.as_view()),
    # path('', Snippets.as_view())
]