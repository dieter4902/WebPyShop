from django.shortcuts import render, redirect
from .forms import ProductForm, SearchForm, SearchStarsForm, CommentForm
from .models import Product, Comment
from Shoppingcart.models import ShoppingCart


def product_list(request):
    all_the_products = Product.objects.all()
    context = {'all_the_products': all_the_products}
    return render(request, 'product-list.html', context)


def product_detail(request, **kwargs):
    product_id = kwargs['pk']
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        form.instance.user = request.user
        form.instance.product = product
        if form.is_valid():
            form.save()
        else:
            print("TODO")
            myuser = request.user
            ShoppingCart.add_item(myuser, product)

    comments = Comment.objects.filter(product=product)
    context = {'that_one_product': product,
               'comments_for_that_one_product': comments,
               'voteCount': product.get_votes_count(),
               'voteScore': product.get_votes_score(),
               'comment_form': CommentForm}
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
        search_string_description = request.POST['description']
        search_string_brand = request.POST['brand']
        search_stars = request.POST['stars']
        products_found = Product.objects.all()
        print(request.POST)
        # print(search_string_name)
        # bei post auf alle zugreife, volle in array stecken, mit for loop durchgehen und langsam filtern
        if search_string_name:
            products_found = products_found.filter(name__contains=search_string_name)
            print(type(products_found))
            print(products_found)

        if search_string_description:
            products_found = products_found.filter(description__contains=search_string_description)
            print(type(products_found))
            print(products_found)

        if search_string_brand:
            products_found = products_found.filter(brand__contains=search_string_brand)
            print(type(products_found))
            print(products_found)

        if search_stars:
            products_found = products_found.filter(vote__stars__gte=search_stars)
            print(search_stars)

        form_in_function_based_view = SearchForm()
        form_test = SearchStarsForm()
        context = {'form': form_in_function_based_view,
                   'formStar': form_test,
                   'products_found': products_found,
                   'show_results': True}
        return render(request, 'product-search.html', context)

    else:
        form_in_function_based_view = SearchForm()
        form_test = SearchStarsForm()
        context = {'form': form_in_function_based_view,
                   'formStar': form_test,
                   'show_results': False}
        return render(request, 'product-search.html', context)


def vote(request, pk: str, rating: int):
    product = Product.objects.get(id=int(pk))
    user = request.user
    product.vote(user, rating)
    return redirect('product-detail', pk=pk)


def comment_vote(request, pk: str, up_or_down: str):
    comment = Comment.objects.get(id=int(pk))
    user = request.user
    comment.vote(user, up_or_down)
    return redirect('product-delete', pk=comment.product.id)


def comment_delete(request, pk: str):
    comment = Comment.objects.get(id=int(pk))
    user = request.user
    comment.c_delete(user)
    return redirect('product-detail', pk=comment.product.id)
