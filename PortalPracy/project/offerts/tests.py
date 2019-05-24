from django.test import TestCase
from django.urls import resolve
from .views import home
# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        # resolve is the function Django uses to resolve URLs and find what view function they should map to.
        # checking that resolve, when called with “/” finds a function called home
        found = resolve('/')
        self.assertEqual(found.func, home)
