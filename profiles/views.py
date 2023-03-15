from django.shortcuts import render

from .forms import ProfileCreateForm, RawProfileForm
from .models import Profile

# Create your views here.
def profile_detail_view(request):
    obj = Profile.objects.get(id=1)
    context = {
        'object': obj 
    }
    return render(request, "profiles/profile_detail.html", context)

def profile_create_view(request):
    my_form = RawProfileForm()
    if request.method == "POST":
        my_form = RawProfileForm(request.POST)
        if my_form.is_valid():
            # now the data is good
            print(my_form.cleaned_data)
            Profile.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        "form": my_form
    }
    return render(request, "profiles/profile_create.html", context)

# def profile_create_view(request):
#     print(request.POST)
#     my_new_title = request.POST.get('title')
#     # Profile.objects.create(title=my_new_title)
#     context = {}
#     return render(request, "profiles/profile_create.html", context)

# def profile_create_view(request):
#     form = ProfileCreateForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProfileCreateForm()

#     context = {
#         'form': form 
#     }
#     return render(request, "profiles/profile_create.html", context)
    