from django.db import models


# Create your models here.
class Enquiry(models.Model):
    """
    Stores a single enquiry from a site visitor
    """
    enquirer_name = models.CharField('name', max_length=200)
    enquirer_email = models.EmailField('email')
    enquirer_phone = models.CharField('phone', max_length=20)
    content = models.TextField('enquiry')
    read = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]
        verbose_name_plural = "enquiries"
    
    def __str__(self):
        return f"{self.enquirer_name} [{self.enquirer_email}] - {self.created_on}"
