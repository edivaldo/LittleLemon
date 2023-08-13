from django.test import TestCase
from .models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
         item = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
         self.assertEqual(item.Title, "IceCream")

"""
class MenuViewTest(TestCase):
    def setup(self):
         item = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
         item = Menu.objects.create(Title="Chocolate", Price=60, Inventory=100)
         item = Menu.objects.create(Title="Pizza", Price=40, Inventory=100)
         item = Menu.objects.create(Title="Candy", Price=20, Inventory=100)
    def test_getall(self):
         self.setup()
         self.assertEqual(Menu.objects.all(), {"IceCream : 80"})
         """