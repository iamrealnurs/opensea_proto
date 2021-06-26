from django.test import TestCase
from main.models import Product, Seller
from django.contrib.auth.models import User

import pprint

if Seller.objects.all():
    Seller.objects.all().delete()

sel_1 = Seller.objects.create_user(username="Нурсултан Кужагалиев", password="123456", blockchain_network_name='Ethereum', blockchain_wallet_address='aserfe12343wreqrw')
sel_1.save()

sel_2 = Seller.objects.create_user(username="Михаил Бородин", password="123456", blockchain_network_name='Ethereum', blockchain_wallet_address='wiy4cgnr34crq1231231')
sel_2.save()

def product_gen():
    from main.models import Product
    import random
    product_title_list = ["Стол", "Стул", "Кресло", "Лампа", "Кровать", "Ковер", "Картина", "Пазл"]

    for number in range(1, 40):
        product_title = random.choice(product_title_list)
        product_obj = Product(title=f"{product_title} N{number}",
                             description=f"Описание {product_title} N{number}",
                             price=random.randint(100, 900), seller=sel_1,
                              token_id = random.randint(1000000000000000, 10000000000000000))
        product_obj.save()

def product_print():
    from main.models import Product
    for product_o in list(Product.objects.all()):
        print("----------------")
        print(f"Вещь {product_o.id} - {product_o.title} - {product_o.description} - {product_o.price}")

def product_deleter():
    from main.models import Product
    Product.objects.all().delete()

product_gen()
product_print()
# product_deleter()

print("----------------")
