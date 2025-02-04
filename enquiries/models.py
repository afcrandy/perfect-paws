from django.db import models


# Create your models here.
class Enquiry(models.Model):
    """
    Models a single enquiry submitted by a site visitor.
    
    **Attributes:**
        enquirer_name (str): The name of the person making the enquiry.
        enquirer_email (str): The email of the person making the enquiry.
        enquirer_phone (str): The phone number of the enquirer.
        content (str): The content of the enquiry or question.
        read (bool): Whether the enquiry has been read by the site owner.
        created_on (datetime): Timestamp for when the enquiry was created.
    
    **Meta:**
        ordering: Orders enquiries by creation date in descending order.
        verbose_name_plural: Specifies the plural form of the model name.
    """
    enquirer_name = models.CharField('name', max_length=200)
    enquirer_email = models.EmailField('email')
    enquirer_phone = models.CharField('phone', max_length=20)
    content = models.TextField('enquiry')
    read = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]
        verbose_name_plural = "enquiries"
    
    def __str__(self):
        return f"{self.enquirer_name} [{self.enquirer_email}] - {self.created_on}"
