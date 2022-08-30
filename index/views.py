from cgitb import reset
from tabnanny import check
from unicodedata import category
from . import models
from django.shortcuts import render, redirect
from django.http import HttpResponse
import telebot

# Create your views here.

def index(request):
    all_products = models.Product.objects.all()
    categories = models.Category.objects.all()
    return render(request, 'index.html', {'products': all_products, 'categories': categories})


def about(request):
    return HttpResponse('About us')

def conact(request):
    return HttpResponse('Contact')

def about_prodcut(request, pk):
    product = models.Product.objects.get(product_name= pk)
    return render(request, 'about_product.html', {'product': product})
def user_card(request):
    user_products = models.UserCart.objects.filter(user_id= request.user.id)
    total_amount = sum([total.quantity*total.product.product_price for total in user_products])
    return render(request, 'user_cart.html', {'product': user_products, 'total': total_amount})


    
def add_pr_to_cart(request, pk):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        #Dobavlyaem v korzinu
        user_id = request.user.id   
        product_id = models.Product.objects.get(id=pk)
        if product_id.product_count >= quantity:
        #Umenshenie kolichesva na skalde            
            product_id.product_count -= quantity
            product_id.save()
            #Proverka est li etot tovar v korzine
            checker = models.UserCart.objects.filter(user_id=user_id, product=product_id)
            #elsi net tovara sozdaem
            if not checker:
                models.UserCart.objects.create(user_id=user_id, product=product_id, quantity=quantity)
            # Esli est to uvilichivaet
            else:
                pr_to_add = models.UserCart.objects.get(user_id=user_id, product=product_id)
                pr_to_add.quantity += quantity
                pr_to_add.save() 
            return redirect('/')
        else:
            return redirect(f'/product/{product_id.product_name}')

       
def delete_from_cart(request, pk):
    if request.method == 'POST':
        product_to_delete = models.Product.objects.get(id=pk)
        user_cart = models.UserCart.objects.get(product= product_to_delete, user_id=request.user.id) 
        product_to_delete.product_count += user_cart.quantity 
        user_cart.delete()
        
        product_to_delete.save()
        return redirect('/cart')
# Otpravit zakaz
def confirm_order(request, pk):
    if request.method == "POST":
        user_cart = models.UserCart.objects.filter(user_id = request.user.id)
        full_message = 'New Order: \n\n'
        for item in user_cart:
            full_message += f' Product: {item.product.product_name}: {item.quantity}'
        total = [i.product.product_price*i.quantity for i in user_cart]
        full_message += f'\n\n All Order:{sum(total)}'
        if len(full_message) > 15:
                #Podkluchenie k botu
            bot = telebot.TeleBot('5612532304:AAH0Ksh9VByPPFpnH2P7WJ6NGTzB8K3emEg')
            bot.send_message(1503117376, f'{full_message} сум')
        
        user_cart.delete()
        print(full_message)
        return redirect('/') 
        
