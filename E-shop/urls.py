from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth import views

from apps.cart.webhook import webhook
from apps.cart.views import cart_detail, success
from apps.core.views import disable_product, enable_product, frontpage, contact, about
from apps.order.views import admin_order_pdf, user_order_list
from apps.store.views import product_detail, category_detail, search, search_Manage, manager_category
from apps.userprofile.views import signup, myaccount

# from apps.newsletter.api import api_add_subscriber
from apps.store.api import api_add_to_cart, api_remove_from_cart, create_checkout_session, api_checkout #, validate_payment
from apps.core.views import productManagePage,order_list
from .sitemaps import StaticViewSitemap, CategorySitemap, ProductSitemap
from apps.store.views import productCreateView, editProductView, deleteProductView

sitemaps = {'static': StaticViewSitemap, 'product': ProductSitemap, 'category': CategorySitemap}

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('', frontpage, name='frontpage'),
    path('orders/', order_list, name='order_list'),
    path('user_orders/', user_order_list, name='user_order_list'),
    path('search/', search, name='search'),
    path('search_manage/', search_Manage, name='searchManage'),
    path('cart/', cart_detail, name='cart'),
    path('hooks/', webhook, name='webhook'),
    path('cart/success/', success, name='success'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),
    path('admin/admin_order_pdf/<int:order_id>/', admin_order_pdf, name='admin_order_pdf'),

    # Auth

    path('myaccount/', myaccount, name='myaccount'),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    # API

    path('api/create_checkout_session/', create_checkout_session, name='create_checkout_session'),
    #path('api/validate_payment/', validate_payment, name='validate_payment'),
    path('api/add_to_cart/', api_add_to_cart, name='api_add_to_cart'),
    path('api/remove_from_cart/', api_remove_from_cart, name='api_remove_from_cart'),
    # path('api/add_subscriber/', api_add_subscriber, name='api_add_subscriber'),
    path('api/checkout/', api_checkout, name='api_checkout'),

    #projectManager

    path('productManager/', productManagePage, name="productManager"),
    path('productManager/add/', productCreateView.as_view(), name="addProduct"),
    path('productManager/edit/<int:pk>/', editProductView.as_view(), name='editProduct'),
    path('productManager/delete/<int:pk>/', deleteProductView.as_view(), name='deleteProduct'),
    path('productManager/<slug:slug>/', manager_category, name='manager_category'),
    path('disable_product/<int:product_pk>/', disable_product, name='disableProduct'),
    path('enable_product/<int:product_pk>/', enable_product, name='enableProduct'),

    # Store

    path('<slug:category_slug>/<slug:slug>/', product_detail, name='product_detail'),
    path('<slug:slug>/', category_detail, name='category_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
