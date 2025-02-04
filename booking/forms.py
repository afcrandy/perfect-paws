from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = (
            'service',
            'date',
            'time',
            'dog_name',
            'dog_breed',
            'dog_size',
            'additional_notes',
        )
        widgets = {
            'dog_name': forms.TextInput(
                attrs={
                    'placeholder': 'Tilly',
                }
            ),
            'dog_breed': forms.TextInput(
                attrs={
                    'placeholder': 'Cockapoo',
                }
            ),
            'additional_notes': forms.Textarea(
                attrs={
                    'placeholder': 'e.g. Tilly has a lot of matting around her ears'
                }
            ),
        }

class BookingDateTimeForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = (
            'date',
            'time',
        )
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'id': 'datepicker',
                }
            ),
            'time': forms.Select(
                attrs={
                    'id': 'timepicker',
                }
            ),
        }

class BookingDogInfoForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = (
            'dog_name',
            'dog_breed',
            'dog_size',
            'additional_notes'
        )
        widgets = {
            'dog_name': forms.TextInput(
                attrs={
                    'placeholder': 'Tilly',
                    'id': 'dog-name',
                    'data-booking-form-id': 'id_dog_name',
                }
            ),
            'dog_breed': forms.TextInput(
                attrs={
                    'placeholder': 'Cockapoo',
                    'id': 'dog-breed',
                    'data-booking-form-id': 'id_dog_breed',
                }
            ),
            'dog_size': forms.Select(
                attrs={
                    'id': 'dog-size',
                    'data-booking-form-id': 'id_dog_size',
                }
            ),
            'additional_notes': forms.Textarea(
                attrs={
                    'placeholder': 'e.g. Tilly has a lot of matting around her ears',
                    'id': 'dog-additional-notes',
                    'data-booking-form-id': 'id_additional_notes',
                }
            ),
        }
