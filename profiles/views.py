from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProfileCreateForm, RawProfileForm
from .models import Profile

# Create your views here.

def render_initial_data(request):
    initial_data = {
        'username': 'default_unknown_user'
    }
    obj = Profile.objects.get(id=1)
    form = ProfileCreateForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "profiles/profile_create.html", context)

def profile_detail_view(request):
    obj = Profile.objects.get(id=1)
    context = {
        'object': obj 
    }
    return render(request, "profiles/profile_detail.html", context)

# def profile_create_view(request):
#     my_form = RawProfileForm()
#     if request.method == "POST":
#         my_form = RawProfileForm(request.POST)
#         if my_form.is_valid():
#             # now the data is good
#             print(my_form.cleaned_data)
#             Profile.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request, "profiles/profile_create.html", context)

# def profile_create_view(request):
#     print(request.POST)
#     my_new_title = request.POST.get('title')
#     # Profile.objects.create(title=my_new_title)
#     context = {}
#     return render(request, "profiles/profile_create.html", context)

def profile_create_view(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProfileCreateForm()

    context = {
        'form': form 
    }
    return render(request, "profiles/profile_create.html", context)


def dynamic_lookup_view(request, id):
    # obj = Profile.objects.get(id=id)
    obj = get_object_or_404(Profile, id=id)
    # try:
    #     obj = Profile.objects.get(id=my_id)
    # except Profile.DoesNotExist:
    #     raise Http404
    context = {
        "object": obj
    }
    return render(request, "profiles/profile_detail.html", context)


def profile_delete_view(request, id):
    obj = get_object_or_404(Profile, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../../create/')
    context = {
        'object': obj
    }
    return render(request, "profiles/profile_delete.html", context)
