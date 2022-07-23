from django.shortcuts import render, redirect
from .forms import ProductForm, SearchForm
from .models import Product
from Shoppingcart.models import ShoppingCart


def product_list(request):
    all_the_products = Product.objects.all()
    context = {'all_the_products': all_the_products}
    return render(request, 'product-list.html', context)


def product_detail(request, **kwargs):
    product_id = kwargs['pk']
    product = Product.objects.get(id=product_id)
    
    if request.method == 'POST':
        myuser = request.user
        ShoppingCart.add_item(myuser, product)

    context = {'that_one_product': product,
               'voteCount': product.get_votes_count(),
               'voteScore': product.get_votes_score()}
    return render(request, 'product-detail.html', context)


def product_create(request):
    if request.method == 'POST':
        form_in_my_function_based_view = ProductForm(request.POST)
        form_in_my_function_based_view.instance.user = request.user
        if form_in_my_function_based_view.is_valid():
            form_in_my_function_based_view.save()
        else:
            pass
        return redirect('all-products')
    else:
        form_in_my_function_based_view = ProductForm()
        context = {'form': form_in_my_function_based_view}
        return render(request, 'product-create.html', context)


def product_delete(request, **kwargs):
    if request.method == 'POST':
        product_id = kwargs['pk']
        Product.objects.get(id=product_id).delete()
        return redirect('all-products')
    else:
        product_id = kwargs['pk']
        that_one_product = Product.objects.get(id=product_id)
        context = {'one_product': that_one_product}
        return render(request, 'product-delete.html', context)


def product_search(request):
    if request.method == 'POST':
        search_string_name = request.POST['name']
        print(search_string_name)
        products_found = Product.objects.filter(name__contains=search_string_name)
        print(products_found)

        form_in_function_based_view = SearchForm()
        context = {'form': form_in_function_based_view,
                   'products_found': products_found,
                   'show_results': True}
        return render(request, 'product-search.html', context)

    else:
        form_in_function_based_view = SearchForm()
        context = {'form': form_in_function_based_view,
                   'show_results': False}
        return render(request, 'product-search.html', context)


def vote(request, pk: str, rating: int):
    product = Product.objects.get(id=int(pk))
    user = request.user
    product.vote(user, rating)
    return redirect('product-detail', pk=pk)
