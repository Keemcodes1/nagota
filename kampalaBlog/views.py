from django.shortcuts import render,redirect
from .models import Destination,Message
# Create your views here.

def index(request):
    dests = Destination.objects.all()
    #name = Destination.objects.all()
    #image = Destination.objects.all()
    #price = Destination.objects.all()
    #special_offer = Destination.objects.all()
   # context = {'name':name,'image':image,'price':price,'special_offer':special_offer}
    
    #return render(request, 'index.html',{'price': 700})
    #return render(request, 'index.html', {'context': context})
    return render(request, 'index.html', {'dests':dests})
def subscribe(request):
    if request.method == 'POST':
        messages = Message.objects.all()
        comment= request.POST.get('comment')
        return redirect('index')
    context = {'comment':comment,'messages':messages}
    return render (request,'subscribe.html',{'context':context})


def about(request):
    
    return render(request,'about.html')

from django.core.paginator import Paginator
from .models import Products

def products(request):
    product_list = Products.objects.all()
    paginator = Paginator(product_list, 10)  # Show 10 products per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products.html', {'page_obj': page_obj})

def products1(request):
    return render(request,'products1.html')
def products2(request):
    return render(request,'products2.html')
def products3(request):
    return render(request,'products3.html')
def products4(request):
    return render(request,'products4.html')
def products5(request):
    return render(request,'products5.html')

def single_product(request):
    return render(request,'single_product.html')

def contact(request):
    return render(request,'contact.html')
def blog(request):
    return render(request,'blog.html')