from django.shortcuts import render

from .models import ProductPrice

# Create your views here.
def homepage(request):
	return render(request, 'store/index.html')

def contact(request):
	return render(request, 'store/contact.html')

def product_list(request):
	product_list = ProductPrice.objects.all()
	context = {'product_list' : product_list}
	return render(request, 'store/product_list.html', context)