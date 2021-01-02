from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()
    avatar = models.ImageField(upload_to='avatar/')

    def __str__(self):
        return f'{self.last_name}({self.email})'
class Transaction(models.Model):
    to = models.ForeignKey(Client, related_name='sent', on_delete=models.CASCADE)
    frm = models.ForeignKey(Client, related_name='recieved', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=50, decimal_places=3)

    def __str__(self):
        return f'Sent (${self.amount}) to {self.to}'