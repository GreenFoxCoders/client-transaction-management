from django.test import SimpleTestCase
from django.urls import reverse, resolve

from ctapp.views import *
class TestURLs(SimpleTestCase):

    def test_home_url_is_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)
    
    def test_clients_url_is_resolves(self):
        url = reverse('clients')
        self.assertEquals(resolve(url).func, clients)
    
    def test_transactions_url_is_resolves(self):
        url = reverse('transactions')
        self.assertEquals(resolve(url).func, transactions)
    
    def test_add_client_url_is_resolves(self):
        url = reverse('add_client')
        self.assertEquals(resolve(url).func, add_client)

    def test_add_transaction_url_is_resolves(self):
        url = reverse('add_transaction')
        self.assertEquals(resolve(url).func, add_transaction)
    

    
    