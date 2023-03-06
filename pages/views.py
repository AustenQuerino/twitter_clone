from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})

def contact_view(request, *arg, **kwargs):
    return render(request, 'contact.html', {})

def about_view(request, *arg, **kwargs):
    my_context = {
        'my_text': 'This is for learning Django',
        'my_number': 531684,
        'my_list': [1, 2, 34, 567, 89]
    }
    return render(request, 'about.html', my_context)


