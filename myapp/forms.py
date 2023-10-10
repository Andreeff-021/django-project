from django import forms
from .models import Category


categories = [category.name for category in Category.objects.all()]


class UserForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=11)
    address = forms.CharField(max_length=200)


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    category = forms.CharField(max_length=50)
    description = forms.CharField(max_length=200)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    quantity = forms.IntegerField()
    rating = forms.DecimalField(max_digits=3, decimal_places=2)
    image = forms.ImageField()
