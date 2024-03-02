from django.urls import path
from .views import CreateShortURL, RedirectOriginalURLView

urlpatterns = [
    path('', CreateShortURL.as_view()),
    path('<str:short_url>/', RedirectOriginalURLView.as_view())
]