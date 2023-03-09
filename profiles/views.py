from django.shortcuts import render

from .forms import ProfileCreateForm
from .models import Profile

# Create your views here.
def profile_detail_view(request):
    obj = Profile.objects.get(id=1)
    context = {
        'object': obj 
    }
    return render(request, "profiles/profile_detail.html", context)

def profile_create_view(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form 
    }
    return render(request, "profiles/profile_create.html", context)
    