
class Cart:
    def __init__(self, request):
        # Save User Request
        self.request = request
        self.session = request.session

        # Getting Cart From Session
        cart = self.session.get('cart')

        # If User Don't have Cart , Create a New One
        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart


