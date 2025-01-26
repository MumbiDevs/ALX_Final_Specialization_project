from store.models import Product


class Cart():
    def __init__(self, request):
        self.session = request.session
        
        #get current session if exists, 
        cart = self.session.get('session_key')

        #if not create one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        #make sure session is available on all pages
        self.cart = cart     

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        #do some logic
        if product_id in self.cart:
            pass
        else:
           # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

            self.session.modified = True
           

    def get_prods(self):
        #get ids from cart
        product_ids = self.cart.keys()
        #use IDS to lookup products in database
        products = Product.objects.filter(id__in=product_ids)

        #return looked up products
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities

    def __len__(self):
        return len(self.cart)
    


    

    