from django.test import TestCase
from django.test import Client as Tester
from django.urls import reverse
from django.contrib.auth import login

from ctapp.views import Client, Transaction

class TestViews(TestCase):

    def setUp(self):
        self.tester = Tester()
        self.home_url = reverse('home')
        self.clients_url = reverse('clients')
        self.transactions_url = reverse('transactions')
        self.login_url = reverse('login')

    def test_home(self):
        response = self.tester.get(self.home_url)
        self.assertEquals(response.status_code, 302)

    def test_clients(self):
        response = self.tester.get(self.clients_url)

        self.assertEquals(response.status_code, 302)

    def test_transactions(self):
        response = self.tester.get(self.transactions_url)

        self.assertEquals(response.status_code, 302)

    # all this test cases are 302 as all the pages are required login access. There we have a lot more possible test case to write however,
    # due time constraint and not writing for a real project(project was for demonstration purpose) I've opted for skipping some.