from django.shortcuts import render
from django.views.generic import ListView

from .models import Item, ItemImage

class ItemListView(ListView):
    model = Item
