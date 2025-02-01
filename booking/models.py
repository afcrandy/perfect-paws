from django.db import models
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField


# Create your models here.
class Service(models.Model):
    """
    Stores a single service provided by Perfect Paws
    """
    name = models.CharField('service name', max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    active = models.BooleanField(default=False)
    duration = models.PositiveIntegerField('service duration (in minutes)')
    image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    def clean(self):
        super().clean()
        if self.cost < 0.0:
            raise ValidationError({'cost': 'Cost cannot be less than 0'})
        if self.duration > 480:
            raise ValidationError({'duration': "Duration cannot be longer than 480 minutes (8 hours)"})
