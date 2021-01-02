from django.forms import ModelForm

from .models import Client, Transaction

class AddClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class AddTransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'