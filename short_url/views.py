from django.shortcuts import render, redirect
from django.http import Http404
from .models import Url
from .forms import UrlForm
import random
import string
from django.views import View


# API:- genearte Short URL
class CreateShortURL(View):

    # This method give the random 6 digit string
    def generate_short_url(self):
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choice(characters) for _ in range(6))
        return short_url
    
    # Called when request is get
    def get(self, request):
        form = UrlForm()
        return render(request, 'short\create_short_url.html', {'form': form})
    
    # Called when request is post
    def post(self, request):
        form =UrlForm(request.POST)
        if form.is_valid():
            try:
                form_data = dict(form.data)
                original_url = form_data['original_url'][0]
                url = Url.objects.filter(original_url=original_url)

                if(url.exists()):
                    short_url = url[0].short_url
                else:
                    short_url = self.generate_short_url()
                    while Url.objects.filter(short_url=short_url).exists():
                        short_url = self.generate_short_url()
                    url = Url.objects.create(original_url=original_url, short_url=short_url)
                return render(request, 'short\short_url.html', {'short_url': short_url})
            except:
                raise Http404('Some thing went wrong')
        
        return render(request, 'short\create_short_url.html', {'form': form})
    

# API:- Redirect to the original url
class RedirectOriginalURLView(View):
    def get(self, request, short_url):
        try:
            url = Url.objects.get(short_url=short_url)
            return redirect(url.original_url)
        except Url.DoesNotExist:
            raise Http404('Short URL does not exist')

