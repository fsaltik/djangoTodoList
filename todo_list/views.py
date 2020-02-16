from django.shortcuts import render,redirect
from .forms import ListForm
from .models import List
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.

def home(request):

    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, 'item has been added to list')
            return render(request, 'home.html', {'all_items': all_items})

    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items' : all_items})

def about(request):
   context = {'name': 'f', 'last_name': 'saltik' }
   return render(request, 'about.html', context)

def delete(request,list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, 'item has been deleted')
    return redirect('home')

