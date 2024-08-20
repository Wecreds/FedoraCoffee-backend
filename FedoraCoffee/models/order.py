from django.db import models
from django.utils import timezone
from .client import Client

class Order(models.Model):
    class Status(models.IntegerChoices):
        IN_PROGRESS = 1, 'In Progress'
        PAYING = 2, 'Paying'
        DONE = 3, 'Done'

    status = models.IntegerField(choices=Status.choices, default=Status.IN_PROGRESS)
    data = models.DateTimeField(default=timezone.now)
    client = models.ForeignKey(
        Client, on_delete=models.PROTECT, related_name="orders", blank=False
    )

    def __str__(self):
        return f'({self.get_status_display()}) {self.client} - {self.data}'