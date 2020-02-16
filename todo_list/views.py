from django.shortcuts import render
from .forms import ListForm
from .models import List


# Create your views here.

def home(request):

    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            return render(request, 'home.html', {'all_items': all_items})

    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items' : all_items})

def about(request):
   context = {'name': 'f', 'last_name': 'saltik' }
   return render(request, 'about.html', context)
