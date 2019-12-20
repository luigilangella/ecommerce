from django.test import TestCase
from .models import Product
# Create your tests here.
class ProductTest(TestCase):
    """
        Here we'll be running the
        tests against our product
        model
    """
    def test_product_name(self):
        name = Product(name='Mobile')
        self.assertEqual(str(name),'Mobile')
