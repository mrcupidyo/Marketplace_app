from urllib import request
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Item, Category
from .forms import ItemForm, ItemUpdateForm

# Create your views here.
#browse items
from django.db.models import Q
from django.shortcuts import render
from .models import Item, Category

def items(request):
    categories = Category.objects.all()
    selected_categories = request.GET.getlist('category')
    query = request.GET.get('query', '')

    # start with all available items
    items = Item.objects.filter(is_available=True)

    # filter by selected categories
    if selected_categories:
        items = items.filter(category__id__in=selected_categories)

    # filter by search query
    if query:
        items = items.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    items = items.order_by('-created_at')

    return render(request, 'item/items.html', {
        'items': items,
        'categories': categories,
        'query': query,
        'selected_categories': selected_categories
    })


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category).exclude(pk=item.pk)[:4]
    return render(request, 'item/detail.html', {'item': item, 'related_items': related_items})
@login_required
def create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk=item.pk)
    else:
        form = ItemForm()
    return render(request, 'item/form.html', {'form': form})
@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard:index')
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = ItemUpdateForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:detail', pk=item.pk)
    else:
        form = ItemUpdateForm(instance=item)
    return render(request, 'item/form.html', {'form': form, 'title': 'Edit Item'})