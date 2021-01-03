from django.test import TestCase
import tempfile

from ctapp.models import Client, Transaction

class TestModels(TestCase):

    def setUp(self):
        image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        self.client = Client.objects.create(
            first_name='First Name',
            last_name='Last Name',
            email='email@email.com',
            avatar=image
        )

    def test_client_email(self):
        self.assertEquals(self.client.email, 'email@email.com')
    
    def test_transaction(self):
        transaction = Transaction.objects.create(
            to=self.client,
            amount=10000,
        )
        self.assertEquals(transaction.to, self.client)
        self.assertEquals(transaction.amount, 10000)