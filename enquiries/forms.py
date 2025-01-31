from .models import Enquiry
from django import forms


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = (
            'enquirer_name',
            'enquirer_email',
            'enquirer_phone',
            'content',
        )
        labels = {
            'content': 'Message'
        }
        widgets = {
            'enquirer_name': forms.TextInput(attrs={'placeholder': 'e.g. Bilbo Baggins'}),
            'enquirer_email': forms.EmailInput(attrs={'placeholder': 'e.g. bilbo.baggins@email.com'}),
            'enquirer_phone': forms.TextInput(attrs={'placeholder': '07123 456 789'}),
            'content': forms.Textarea(attrs={'placeholder': """Hi,

I would like to know how much it would cost to groom a middle-aged hobbit

Thanks,
Bilbo
                                            """}),
        }
