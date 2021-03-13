def storage_upload(x,y):
    return 0


def add(self, product, quantity=1, update_quantity=False):
    """Добавление товара в корзину или обновление его количества."""
    product_id = str(product.id)
    if product_id not in self.cart:
        self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
    if update_quantity:
        self.cart[product_id]['quantity'] = quantity
    else:
        self.cart[product_id]['quantity'] += quantity
        self.save()
    
    def save(self):
        # Помечаем сессию как измененную
        self.session.modified = True