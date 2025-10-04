from django.shortcuts import get_object_or_404, render
from item.models import Item, Category
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user).order_by('-created_at')
    categories = Category.objects.all()
    return render(request, '.dashboard.html', {'items': items, 'categories': categories})
