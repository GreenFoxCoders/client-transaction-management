from django.test import TestCase
import tempfile
from ctapp.forms import AddClientForm, AddTransactionForm
from ctapp.models import Client
class TestForms(TestCase):

    def test_add_transaction_form_valid_data(self):
        image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        client = Client.objects.create(
            first_name='First Name',
            last_name='Last Name',
            email='email@email.com',
            avatar=image
        )
        form = AddTransactionForm(data={
            'to': client,
            'amount': 1500,
        })
        self.assertTrue(form.is_valid())

    def test_add_transaction_invalid_data(self):
        form = AddTransactionForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
