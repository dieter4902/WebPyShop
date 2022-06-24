from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product


def product_list(request):
    all_the_products = Product.objects.all()
    context = {'all_the_products': all_the_products}
    return render(request, 'product-list.html', context)


def product_detail(request, **kwargs):
    product_id = kwargs['pk']
    product = Product.objects.get(id=product_id)

    context = {'that_one_product': product,
               'upvotes': product.get_upvotes_count(),
               'downvotes': product.get_downvotes_count()}
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


def vote(request, pk: str, up_or_down: str):
    product = Product.objects.get(id=int(pk))
    user = request.user
    product.vote(user, up_or_down)
    return redirect('product-detail', pk=pk)
