import django
from django.shortcuts import render
from item.models import Item, Category
from django.contrib.auth.models import User
from .forms import SignInForm, SignUpForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
    items = Item.objects.filter(is_available=True).order_by('-created_at')[:10]
    categories = Category.objects.all()
    return render(request, 'index.html', {'items': items, 'categories': categories})
def contact(request):
    return render(request, 'contact.html')
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
def signin(request):
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            django.contrib.auth.login(request, form.get_user())
            return redirect('core:index')
    else:
        form = SignInForm()
    return render(request, 'signin.html', {'form': form})
