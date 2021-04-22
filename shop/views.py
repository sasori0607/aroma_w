from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from django.http import JsonResponse
from django.core.paginator import Paginator

from django.shortcuts import redirect





class Shop_main(ListView):
    paginate_by = 3 #количество элементов на странице
    model = Product
    template_name = 'shop/shop_main.html'
    context_object_name = 'products'
    ordering = ['-id']

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(Shop_main, self).get_context_data(**kwargs)
        ctx['category'] = Category.objects.all()
        return ctx






class Shop_category(ListView, Paginator):

    paginate_by = 2
    template_name = 'shop/shop_category.html'
    ordering = ['-id']
    context_object_name = 'object'

    # Big_list = {
    #     'sanitayzery' : Sanitayzery,
    #     'parfyumy-v-mashinu' :Parfyumy_v_mashinu,
    #     'svechi': Svechi,
    #     'ukhod' : Ukhod,
    #     'sertifikaty' : Sertifikaty,
    #     'aromaty-dlya-doma' : Aromaty_dlya_doma,
    #     'travel-versii' : Travel_versii,
    #     'parfyumy' : Parfyumy,
    #     'nabory' : Nabory,
    #     'bestsellers' : Product,
    #     'novinki' : Product
    # }

    def dispatch(self, request, *args, **kwargs):
        slug = (self.request.path).split('/')[-1]
        self.model = Product
        if slug == 'bestsellers':
            self.queryset = Product.objects.filter(bestsellerTrue=True)
        elif slug == 'novinki':
            self.queryset = Product.objects.filter(newTrue=True)
        else:
            self.queryset = Product.objects.filter(category__slug=slug)
            print(self.queryset, '1999')

        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, *, object_list=None, **kwargs):
        dd = (self.request.path).split('/')[-1]
        print(dd, '123')
        ctx = super(Shop_category, self).get_context_data(**kwargs)
        #ctx = Product.objects.filter(vendorСode__icontains='1234')
        ctx['products'] = Product.objects.all()
        ctx['category'] = Category.objects.all()
        #ctx['slug'] = slug
        return ctx


class Shop_detail_page(DetailView):

    template_name = 'shop/shop_detail.html'

    # CT_MODEL_MODEL_CLASS = {
    #     'bestsellers': Product,
    #     'set': Product,
    #
    # }

    def dispatch(self, request, *args, **kwargs):
        self.model = Product
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):

        ctx = super(Shop_detail_page, self).get_context_data(**kwargs)
        request = self.request
        session_key = request.session.session_key
        if not session_key:
            request.session.cycle_key()
        return ctx




def basket_adding(request):
    data = request.POST
    return_dick = dict()
    slug = data['slug']
    product_by_slug = (Product.objects.filter(slug=slug))[0]

    price = data['price']

    volume = data['volume']
    if volume == 'None':
        volume = 0

    session_key = request.session.session_key

    if not session_key:
        session_key = request.session.cycle_key()




    if not Basket.objects.filter(session_key=session_key, slug=slug, price=price).exists():
        new = Basket(session_key=session_key,
                     slug=slug,
                     title=product_by_slug.title,
                     vendorСode=product_by_slug.vendorСode,
                     category=product_by_slug.category,
                     volume=volume,
                     price=price,
                     quantity=1,
                     img_url=product_by_slug.img.url
                     )
        new.save()
        some = 1

    else:
        var = (Basket.objects.filter(session_key=session_key, slug=slug, price=price))[0]
        var.quantity += 1
        var.save()
        #price = var.price
        some = var.quantity

    return_dick = {'quantity_new': some, 'key': 0, 'price':price, }
    return JsonResponse(return_dick)



def basket_minus(request):
    data = request.POST
    return_dick = dict()
    slug = data['slug']
    price = data['price']

    session_key = request.session.session_key

    new = Basket(session_key=session_key, slug=slug)


    if not Basket.objects.filter(session_key=session_key, slug=slug, price=price).exists():
        new.save()
    else:
        var = (Basket.objects.filter(session_key=session_key, slug=slug, price=price))[0]
        print('123123123123')
        quantity_new = var.quantity
        if quantity_new > 1:
            # quantity_new = quantity_new - 1
            var.quantity = quantity_new - 1
            var.save()
            return_dick = {'quantity_new': var.quantity, 'key': 1, 'price':price}
            return JsonResponse(return_dick)
        else:
            var.delete()
            return_dick = {'key': 0}
            return JsonResponse(return_dick)




def basket(request):

    data = request.POST
    session_key = request.session.session_key
    if not session_key:
        session_key = request.session.cycle_key()
        print(request.session.cycle_key())
    print(data)
    basket_total_quantity = Basket.objects.filter(session_key=session_key)
    sum = 0
    for i in basket_total_quantity:
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
        print(self.request.method)
        ctx = super(you_basket, self).get_context_data(**kwargs)
        request = self.request
        session_key = request.session.session_key
        basket_total_quantity = Basket.objects.filter(session_key=session_key)
        ctx['basket'] = basket_total_quantity
        return ctx


def search(request):
    data = request.POST
    some = Product.objects.filter(title__icontains=data['val'])
    return_dick = {}
    for i in some:
        return_dick[i.title] = i.category.slug + '/' + i.slug
    some2 = Category.objects.filter(title__icontains=data['val'])
    for i in some2:
        return_dick[i.title] = i.slug

    print(return_dick)
    return JsonResponse(return_dick)



def order(request):

    session_key = request.session.session_key
    data = request.POST
    print(session_key)
    print(data['phone'])
    var = (Basket.objects.filter(session_key=session_key))
    products = ''
    for i in var:
        products += 'Товар-'+ i.title + ',  Артикул-' + i.vendorСode + ', Объем-'\
                    + str(i.volume) + ', Количество-' + str(i.quantity) + '\r\n'

    var.delete()
    new = Order(name=data['info'],
                phone=data['phone'],
                comment=data['description'],
                delivery=('Город: ' + data['town'] + '\r\n' + 'Отделение: ' + data['branches']),
                products=products
                )
    new.save()

    return_dick = {}
    return JsonResponse(return_dick)