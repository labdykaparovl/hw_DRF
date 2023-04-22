from app.models import *

c1 = Category.objects.create(name='Продукты')
c2 = Category.objects.create(name='Мыломойка')

Product.objects.create(name='Хлеб', price=20, category=c1)
Product.objects.create(name='Вода', price=45, category=c1)
Product.objects.create(name='моющее средство', price=150, category=c2)
Product.objects.create(name='Порошок', price=320, category=c2)
Product.objects.create(name='Шампунь', price=500, category=c2)