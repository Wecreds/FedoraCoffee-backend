from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)

    def __str__(self):
        return self.name