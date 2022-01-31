from django.core.mail import send_mail
from django.shortcuts import render
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            subject = 'Zamówienie nr {}'.format(order.id)
            message = 'Witaj, {}! Zamówienie, które złożyłes w naszym sklepie ' \
                      'zostanie zrealizowane w ciągu 3 dni roboczych. \n' \
                      'Identyfikator Twojego zamówienia to {}.'.format(order.first_name, order.id)
            send_mail(subject, message, 'shop@mail.com', [order.email])
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
