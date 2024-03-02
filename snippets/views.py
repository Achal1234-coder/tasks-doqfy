from django.shortcuts import render, redirect, HttpResponse
from django.http import Http404
from .models import Snippet
from .forms import SnippetForm
from django.views import View
import uuid


# API:- This API Create Snippet
class CreateSnippet(View):

    def get(self, request):
        form = SnippetForm()
        return render(request, 'snippets/create_snippet.html', {'form': form})
    
    def post(self, request):
        form = SnippetForm(request.POST)
        if form.is_valid():
            shareable_url = str(uuid.uuid4())[:8]  # Generate a unique shareable URL
            snippet = Snippet.objects.create(shareable_url=shareable_url, secret_key=form.data.get('secret_key'), text=form.data.get('text'))
            print(snippet.shareable_url, snippet.text)
            return render(request, 'snippets/shareable_url.html', {'url': 'http://localhost:8000/snippets/{}/'.format(snippet.shareable_url), 'redirect': 'view_snippet/'})
        

#API:- This API Show the Snippet after validation of secreat key
class ViewSnippet(View):
    def get(self, request):
        return render(request, 'snippets/url_secret.html')
    

    def post(self, request):
        try:
            url_end_point = request.POST.get('share_url').split('/')[-2]
            snippet = Snippet.objects.get(shareable_url=url_end_point)
            secret_key = request.POST.get('secret_key')
            if snippet.secret_key and secret_key != snippet.secret_key:
                return HttpResponse('<h1>Invalid Key<h1>')
            return render(request, 'snippets/view_snippet.html', {'snippet': snippet})
        except Snippet.DoesNotExist:
            raise Http404('Snippet not found')
    



