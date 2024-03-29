from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from Customerservice.forms import CommentEditForm
from .forms import ProductForm, SearchForm, CommentForm
from .models import Product, Comment
from Shoppingcart.models import ShoppingCart
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import UpdateView
from .forms import ProductEditForm


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
               'comment_form': CommentForm,
               'pdf': False}
    return render(request, 'product-detail.html', context)


def product_create(request):
    if request.method == 'POST':
        form_in_my_function_based_view = ProductForm(request.POST, request.FILES, )
        form_in_my_function_based_view.instance.user = request.user
        if form_in_my_function_based_view.is_valid():
            form_in_my_function_based_view.save()
        else:
            pass
        return redirect('product-search')
    else:
        form_in_my_function_based_view = ProductForm()
        context = {'form': form_in_my_function_based_view}
        return render(request, 'product-create.html', context)


def product_delete(request, **kwargs):
    if request.method == 'POST':
        product_id = kwargs['pk']
        Product.objects.get(id=product_id).delete()
        return redirect('product-search')
    else:
        product_id = kwargs['pk']
        that_one_product = Product.objects.get(id=product_id)
        context = {'one_product': that_one_product}
        return render(request, 'product-delete.html', context)


def product_search(request):
    products_found = Product.objects.all()
    if request.method == 'POST':
        search_string_name = request.POST['name']
        search_string_description = request.POST['description']
        search_string_brand = request.POST['brand']
        search_stars = request.POST['stars']
        print(request.POST)
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
            products_found = products_found.filter(stars__gte=search_stars)
            print(search_stars)

    form_in_function_based_view = SearchForm()
    context = {'form': form_in_function_based_view,
               'products_found': products_found,
               'show_results': True}
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
    return redirect('product-detail', pk=comment.product.id)


def comment_flag(request, pk: str):
    comment = Comment.objects.get(id=int(pk))
    if request.user:
        comment.set_flag()
        return redirect('product-detail', pk=comment.product.id)
    else:
        return redirect('home')


def comment_flag_remove(request, pk: str):
    print("eee")
    if request.user.is_staff:
        comment = Comment.objects.get(id=int(pk))
        comment.clear_flag()
        return redirect('comment-delete')
    else:
        return redirect('home')


def comment_delete(request, pk: str):
    comment = Comment.objects.get(id=int(pk))
    user = request.user
    comment.c_delete(user)
    return redirect('product-detail', pk=comment.product.id)


def generate_PDF(request, **kwargs):
    product_id = kwargs['pk']
    product = Product.objects.get(id=product_id)
    user = request.user
    comments = Comment.objects.filter(product=product)
    data = {'that_one_product': product,
            'pdf': True,
            'voteCount': product.get_votes_count(),
            'voteScore': product.get_votes_score()}

    template = get_template('product-detail.html')
    html = template.render(dict(data))

    file = open('test.pdf', "w+b")
    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file,
                                encoding='utf-8')

    file.seek(0)
    pdf = file.read()
    file.close()
    return HttpResponse(pdf, 'application/pdf')


class ProductEditView(UpdateView):
    model = Product
    form_class = ProductEditForm
    template_name = 'product-edit.html'
    success_url = reverse_lazy('product-search')

    def get_context_data(self, **kwargs):
        context = super(ProductEditView, self).get_context_data(**kwargs)
        is_staff = False
        myuser = self.request.user
        if not myuser.is_anonymous:
            is_staff = myuser.is_staff
        context['is_staff'] = is_staff
        return context

