from django.db import models

#imports for Post-Save-Receiver:
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Product(models.Model):
    """
    Model for product with basic information.

    Attributes:
        name: Product name
        description: Short product description
        price: Product price (max. 99.99)
    """
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=600)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name 

# Post-Save-Receiver: generates an authentication token for every user   
@receiver(post_save, sender=User)
def generate_auth_token(sender, instance=None, created=False, **kwargs):
    """
    Creates token for user

    Args:
        sender: The model class (User)
        instance: The User instance being saved
        created: True if new record was created
        **kwargs: Additional signal arguments

    Returns:
        None
    """
    if created:
        Token.objects.create(user=instance)
