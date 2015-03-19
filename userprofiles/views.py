from django.shortcuts import render
from .forms import UserCreationEmailForm, EmailAuthenticationForm

# Create your views here.
def signup(request):
    form = UserCreationEmailForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    form = EmailAuthenticationForm(request.POST or None)

    #if form.is_valid():
        #entro

    return render(request, 'signin.html', {'form':form})
