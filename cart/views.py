from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

def cart_summary(request):
    #get cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities - cart.get_quants
    return render(request, "cart_summary.html", {"cart_products":cart_products, "quantities":quantities})

def cart_add(request):
    # Get the cart object
    cart = Cart(request)

    # Check for POST request
    if request.POST.get('action') =='post':
        # Get the product ID from the POST request
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

       

        # Retrieve the product instance from the database
        product = get_object_or_404(Product, id=product_id)
        
        # Add the product to the cart
        cart.add(product=product, quantity=product_qty)

        #get cart quantity
        cart_quantity = cart.__len__()

        # Return a JSON response with the product name
        # response = JsonResponse({'Product Name': product.name})
        response = JsonResponse({'qty': cart_quantity})
        return response

    
def cart_delete(request):
    # Logic for deleting items from the cart
    pass

def cart_update(request):
    # Logic for updating items in the cart
    pass
