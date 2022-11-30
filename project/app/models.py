from django.db import models


class User(models.Model):
    name = models.CharField('name', max_length=120)
    email = models.EmailField('email')
    bday = models.DateField('birthday')
    tax_number = models.CharField('tax number', max_length=120)

    def __str__(self):
        return f'name: {self.name}, email: {self.email}, birthday: {self.bday}, tax number: {self.tax_number}'
