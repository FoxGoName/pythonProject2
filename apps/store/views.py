import random

from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.urls import reverse, reverse_lazy

from apps.cart.cart import Cart

from .models import Product, Category, ProductReview
from django.views.generic import CreateView, UpdateView, DeleteView

def search(request):
    query = request.GET.get('query')
    instock = request.GET.get('instock')
    price_from = request.GET.get('price_from', 0)
    price_to = request.GET.get('price_to', 100000)
    sorting = request.GET.get('sorting', '-date_added')
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)).filter(price__gte=price_from).filter(price__lte=price_to)

    if instock:
        products = products.filter(num_available__gte=1)

    context = {
        'query': query,
        'products': products.order_by(sorting),
        'instock': instock,
        'price_from': price_from,
        'price_to': price_to,
        'sorting': sorting
    }

    return render(request, 'search.html', context)

def product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug)
    product.num_visits = product.num_visits + 1
    product.last_visit = datetime.now()
    product.save()

    # Add review

    if request.method == 'POST' and request.user.is_authenticated:
        stars = request.POST.get('stars', 3)
        content = request.POST.get('content', '')

        review = ProductReview.objects.create(product=product, user=request.user, stars=stars, content=content)

        return redirect('product_detail', category_slug=category_slug, slug=slug)

    #



    imagesstring = "{'thumbnail': '%s', 'image': '%s'}," % (product.thumbnail.url, product.image.url)

    for image in product.images.all():
        imagesstring = imagesstring + ("{'thumbnail': '%s', 'image': '%s'}," % (image.thumbnail.url, image.image.url))

    cart = Cart(request)

    if cart.has_product(product.id):
        product.in_cart = True
    else:
        product.in_cart = False

    context = {
        'product': product,
        'imagesstring': imagesstring,
    }

    return render(request, 'product_detail.html', context)

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()

    context = {
        'category': category,
        'products': products
    }

    return render(request, 'category_detail.html', context)


class productCreateView(CreateView):
    model = Product
    template_name = "add_product.html"
    fields = '__all__'

    def get_success_url(self):
        return reverse("frontpage")

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
    success_url = reverse_lazy('frontpage')


# def search_Manage(request):
#     query = request.GET.get('query')  # 获取搜索关键词

#     if query:
#         results = Product.objects.filter(title__icontains=query)  # 使用icontains过滤器进行模糊匹配
#     else:
#         results = Product.objects.all()  # 如果没有搜索关键词，返回所有对象

#     return render(request, 'search_manage.html', {'results': results, 'query': query})
    
def search_Manage(request):
    query = request.GET.get('query')  # 获取搜索关键词
     
    if query:
     # results = Product.objects.filter(title__icontains=query)  # 使用icontains过滤器进行模糊匹配
     results = Product.objects.filter(Q(title__icontains=query) | Q(id__icontains=query)) 
    else:
        results = Product.objects.all()  # 如果没有搜索关键词，返回所有对象

    products = results  # 将results赋值给products变量

    return render(request, 'search_manage.html', {'results': results, 'query': query, 'products': products})