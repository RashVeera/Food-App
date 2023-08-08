from django.forms.models import BaseModelForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import Item_form
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

def index(request):
    item_list=Item.objects.all()
    context={
        'item_list':item_list,
    }

    return render(request,'fooditems/index.html',context)

class Indexview(ListView):
    model=Item
    template_name='fooditems/index.html'
    context_object_name='item_list'


def item(request):
    return HttpResponse('<h1>Hey, this is my first django Project</h1>')

def detailed_view(request,item_id):
    item=Item.objects.get(pk=item_id)
    context={
        'item':item,
    }
    return render(request,'fooditems/detail.html',context)

class Detail(DetailView):
    model=Item
    template_name='fooditems/detail.html'
    context='item'

def create_item(request):
    item_form=Item_form(request.POST or None)

    if item_form.is_valid():
        item_form.save()
        return redirect('food:index')

    return render(request,'fooditems/create_item.html',{'item_form':item_form} )


# class CreateItem(CreateView):
#     model = Item
#     fields=['item_name','item_desc','price','item_note','image']    
#     template_name='fooditems/create_item.html'
 
#     def form_valid(self,form):
#         form.instance.user_name = self.request.user
 
#         return super().form_valid(form)

def update(request,id):
    item=Item.objects.get(id=id)

    item_form=Item_form(request.POST or None,instance=item)

    if item_form.is_valid():
        item_form.save()
        return redirect('food:index')
    
    return render(request,'fooditems/create_item.html',{'item_form':item_form,'item':item})

def delete(request,id):
    item=Item.objects.get(id=id)

    if request.method=='POST':
        item.delete()
        return redirect('food:index')
    
    return render(request,'fooditems/delete.html',{'item':item})