from django.shortcuts import render

from .models import Profile

# Create your views here.
def profile_detail_view(request):
    obj = Profile.objects.get(id=1)
    context = {
        'object': obj 
    }
    return render(request, "profile/detail.html", context)

