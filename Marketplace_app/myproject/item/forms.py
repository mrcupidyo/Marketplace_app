from django import forms
from .models import Item, Category
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class ItemForm(forms.ModelForm):  
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'category', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-xl', 'placeholder': 'Item Name'}),
            'description': forms.Textarea(attrs={'class': 'w-full p-2 border border-gray-300 rounded-xl', 'placeholder': 'Item Description', 'rows': 4}),
            'price': forms.NumberInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-xl', 'placeholder': 'Item Price'}),
            'category': forms.Select(attrs={'class': 'w-full p-2 border border-gray-300 rounded-xl'}),
            'image': forms.ClearableFileInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-xl'}),
        }
class ItemUpdateForm(forms.ModelForm):  
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'category', 'image', 'is_available']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-xl', 'placeholder': 'Item Name'}),
            'description': forms.Textarea(attrs={'class': 'w-full p-2 border border-gray-300 rounded-xl', 'placeholder': 'Item Description', 'rows': 4}),
            'price': forms.NumberInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-xl', 'placeholder': 'Item Price'}),
            'category': forms.Select(attrs={'class': 'w-full p-2 border border-gray-300 rounded-xl'}),
            'image': forms.ClearableFileInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-xl'}),
        }
