from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegForm
from .models import Profile
from django.contrib import messages
# Create your views here.

@login_required
def register(request):


    if request.method == 'POST':
        form = UserRegForm(request.POST)
        print('ass')
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(username)
            messages.success(request,f'created for{username}')
            return redirect('blog_home')
    else:
        form = UserRegForm()
    
    return render(request,'register.html',{'form':form})
    
@login_required
def profile(request):
    return render(request,'profile.html',{})