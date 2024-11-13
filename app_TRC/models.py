from django.db import models
from django.contrib.auth import get_user_model



TYPE_TRANCIONS = (
    ('incom', 'incom'),
    ('cost', 'cost')
)

user = get_user_model()

class Trancion(models.Model):
    amount = models.IntegerField(null=True)
    descripition = models.TextField(null=True)
    date = models.DateField(null=True)
    code = models.CharField(max_length=10, null=True, unique=True)
    user_TRC = models.ForeignKey(user, on_delete=models.CASCADE, null=True, related_name='Trancionsforuser')
    status_TRC = models.CharField(max_length=5, null=True, choices=TYPE_TRANCIONS)
       
    
    def __str__(self) -> str:
        return self.descripition
