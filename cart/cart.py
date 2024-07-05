
class Cart:
    def __init__(self, request):
        # Save User Request
        self.request = request
        self.session = request.session

        # Getting Cart From Session
        cart = self.session.get('cart')

        # If User Doesn't have Cart , Create a New One
        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def add(self, book, quantity=1):
        book_id = str(book.id)

        if book_id not in self.cart:
            self.cart[book_id] = {'quantity': quantity}
        else:
            self.cart[book_id]['quantity'] += quantity


