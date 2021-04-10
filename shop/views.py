from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from django.http import JsonResponse





class Shop_main(ListView):
    paginate_by = 4 #количество элементов на странице
    model = Product
    template_name = 'shop/shop_main.html'
    context_object_name = 'products'
    ordering = ['-id']

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(Shop_main, self).get_context_data(**kwargs)
        ctx['category'] = Category.objects.all()
        return ctx


class Shop_category(DetailView):
    model = Category
    template_name = 'shop/shop_category.html'
    #context_object_name = 'products_category'



    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(Shop_category, self).get_context_data(**kwargs)
        slug = self.kwargs.get(self.slug_url_kwarg, None)
        ctx['products'] = Product.objects.all()
        ctx['category'] = Category.objects.all()
        ctx['slug'] = slug
        return ctx


class Shop_detail_page(DetailView):

    template_name = 'shop/shop_detail.html'

    CT_MODEL_MODEL_CLASS = {
        'bestsellers': ProductBestsellers,
        'set': ProductSet
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['category']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):

        ctx = super(Shop_detail_page, self).get_context_data(**kwargs)
        request = self.request
        session_key = request.session.session_key
        print(session_key)
        if not session_key:
            request.session.cycle_key()
        print(self.object.category)
        return ctx




def basket_adding(request):
    data = request.POST
    return_dick = dict()
    slug = data['slug']
    print(slug)
    session_key = request.session.session_key
    new = Basket(session_key=session_key, slug=slug)


    if not Basket.objects.filter(session_key=session_key, slug=slug).exists():
        new.save()
    else:
        var = (Basket.objects.filter(session_key=session_key, slug=slug))[0]
        quantity_new = (Basket.objects.filter(session_key=session_key, slug=slug))[0].quantity + 1
        var.quantity = quantity_new
        var.save()
    return_dick = {'quantity_new': quantity_new, 'key': 0}
    return JsonResponse(return_dick)



def basket_minus(request):
    data = request.POST
    return_dick = dict()
    slug = data['slug']

    session_key = request.session.session_key
    new = Basket(session_key=session_key, slug=slug)


    if not Basket.objects.filter(session_key=session_key, slug=slug).exists():
        new.save()
    else:
        var = (Basket.objects.filter(session_key=session_key, slug=slug))[0]
        print('123123123123')
        quantity_new = (Basket.objects.filter(session_key=session_key, slug=slug))[0].quantity
        if quantity_new > 1:
            quantity_new = (Basket.objects.filter(session_key=session_key, slug=slug))[0].quantity - 1
            var.quantity = quantity_new
            var.save()
            return_dick = {'quantity_new': quantity_new, 'key': 1}
            return JsonResponse(return_dick)
        else:
            var.delete()
            return_dick = {'key': 0}
            return JsonResponse(return_dick)




def basket(request):

    data = request.POST
    session_key = request.session.session_key
    print(data)
    basket_total_quantity = Basket.objects.filter(session_key=session_key)
    sum = 0
    for i in basket_total_quantity:
        print(i.slug)
        sum += i.quantity

    return_dick = {'sum': sum}
    return JsonResponse(return_dick)



class you_basket(ListView):
    #paginate_by = 4  количество элементов на странице
    context_object_name = 'object'
    model = Product
    template_name = 'shop/you_basket.html'
    ordering = ['-id']

    def get_context_data(self, *, object_list=None, **kwargs):

        ctx = super(you_basket, self).get_context_data(**kwargs)
        request = self.request
        session_key = request.session.session_key
        basket_total_quantity = Basket.objects.filter(session_key=session_key)
        ctx['Product'] = Product
        deffi = {}
        for i in basket_total_quantity:
            deffi[i.slug] = i.quantity
        ctx['deffi'] = deffi
        print(ctx['deffi'], 'yyyyyyyyyyy')






        return ctx



