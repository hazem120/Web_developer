from django.shortcuts import render
from django.http import HttpResponseRedirect 
from .forms import Follow 
# Create your views here.


def home(request): 
    if request.method == 'POST': 
        form = Follow(request.POST) 
        if form.is_valid(): 
            form.save() 
            return HttpResponseRedirect('/about/')


    else: 
        form = Follow()

    return render(request , 'home/index.html', {'form': form})



def about(request): 
    return render(request , 'home/aboutpage.html') 