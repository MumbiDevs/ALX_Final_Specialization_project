from .cart import Cart

#create context processor for our cart to work on all pages
def cart(request):

    return{'cart': Cart(request)}
