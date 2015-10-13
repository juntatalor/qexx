from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_GET

from products.models import Product, PricedProduct, Category
from payment.models import Currency


def get_pagination(request, object_list, per_page):
    paginator = Paginator(object_list, per_page)

    # Постраничная разбивка
    page = request.GET.get('page')
    try:
        return paginator.page(page)
    except PageNotAnInteger:
        return paginator.page(1)
    except EmptyPage:
        return paginator.page(paginator.num_pages)


@require_GET
def product_index(request):
    # Популярные товары
    popular_products = Product.objects_detailed.filter(popular=True)[:8]
    # Новинки
    new_products = Product.objects_detailed.order_by('-date_created')[:8]

    return render(request, 'products/product_index.html',
                  {'popular_products': popular_products,
                   'new_products': new_products,
                   'currency': Currency.get_main_currency()})


@require_GET
def product_detail(request, slug):
    # Не показываем отсутствующие продукты
    product = get_object_or_404(Product, slug=slug)
    data = PricedProduct.objects_detailed. \
        filter(product=product)

    related_list = [x['id'] for x in product.related_products.values('id')]
    related_products = Product.objects_detailed. \
        filter(id__in=related_list)

    if not data:
        return HttpResponseRedirect(reverse('products:index'))
    if product.type == Product.TYPE_COMMON:
        product_data = data[0]
    elif product.type == Product.TYPE_VARIATIVE:
        product_data = data
    else:
        return HttpResponseRedirect(reverse('products:index'))

    return render(request, 'products/product_detail.html',
                  {'product': product,
                   'product_data': product_data,
                   'product_price': product.get_price_range(),
                   'related_products': related_products})


@require_GET
def category_detail(request, slug):
    # Не показываем отсутствущие категории
    category = get_object_or_404(Category, slug=slug)
    descendants = category.get_descendants(include_self=True)

    # Показываем товары из дочерних категорий
    # Получаем минимальную и максимальную цену на товар
    # Не показываем товары без цены (min_price__isnull=False)
    # Если товар есть в нескольких подкатегориях показываем его один раз (distinct())
    currency = Currency.get_main_currency()
    product_list = Product.objects_detailed. \
        filter(categories__in=descendants). \
        distinct()

    # ToDo: Количество товаров на странице - в настройки
    products = get_pagination(request, product_list, 8)

    return render(request, 'products/category_detail.html', {'category': category,
                                                             'products': products,
                                                             'currency': currency,
                                                             'range': range(1, products.paginator.num_pages + 1)
                                                             })


@require_GET
def product_new(request):
    # Новые
    products = get_pagination(request, Product.objects_detailed.order_by('-date_created'), 12)

    return render(request, 'products/new.html', {'products': products,
                                                 'currency': Currency.get_main_currency(),
                                                 'range': range(1, products.paginator.num_pages + 1)
                                                 })


@require_GET
def product_popular(request):
    # Популярные товары
    products = get_pagination(request, Product.objects_detailed.filter(popular=True), 12)

    return render(request, 'products/popular.html', {'products': products,
                                                     'currency': Currency.get_main_currency(),
                                                     'range': range(1, products.paginator.num_pages + 1)
                                                     })
