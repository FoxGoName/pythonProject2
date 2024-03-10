from django.shortcuts import render

from apps.store.models import Product, Category

from django.views.generic import CreateView, UpdateView, DeleteView

from django.urls import reverse, reverse_lazy

from django.shortcuts import redirect

from django import forms

def frontpage(request):
    products = Product.objects.all()
    featured_categories = Category.objects.all()
    popular_products = Product.objects.all().order_by('-num_visits')[0:4]
    recently_viewed_products = Product.objects.all().order_by('-last_visit')[0:4]

    context = {
        'products': products,
        'featured_categories': featured_categories,
        'popular_products': popular_products,
        'recently_viewed_products': recently_viewed_products
    }

    return render(request, 'frontpage.html', context)

def productManagePage(request):

    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product.html', context)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
class productCreateView(CreateView):
    model = Product
    template_name = "add_product.html"
    form_class = ProductForm

    def get_success_url(self):
        return reverse("productManager")



class editProductView(UpdateView):
    model = Product
    template_name = "edit_product.html"
    fields = '__all__'

    def get_success_url(self):
        product = self.object  # 获取正在编辑的产品对象
        return reverse("product_detail", kwargs={'category_slug': product.category.slug, 'slug': product.slug})

class deleteProductView(DeleteView):
    model = Product
    template_name = "delete_product.html"
    success_url = reverse_lazy('productManager')

from django.shortcuts import render
from apps.order.models import Order
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})