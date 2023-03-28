from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

from .forms import ProfileCreateForm
from .models import Profile

# Create your views here.


def profile_list_view(request):
    queryset = Profile.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "profiles/profile_list_link.html", context)


def profile_create_view(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProfileCreateForm()
    context = {
        'form': form 
    }
    return render(request, "profiles/profile_create.html", context)


def profile_detail_view(request, id):
    obj = get_object_or_404(Profile, id=id)
    context = {
        "object": obj
    }
    return render(request, "profiles/profile_detail.html", context)


def profile_update_view(request, id=id):
    obj = get_object_or_404(Profile, id=id)
    form = ProfileCreateForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        "form": form
    }
    return render(request, "profile/profile_create.html", context)


def profile_delete_view(request, id):
    obj = get_object_or_404(Profile, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../../create/')
    context = {
        'object': obj
    }
    return render(request, "profiles/profile_delete.html", context)


class ProfileListView(ListView):
    template_name = "profiles/profile_list_link.html"
    queryset = Profile.objects.all()

