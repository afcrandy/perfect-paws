# import the superclasses needed for the forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms
from allauth.account.forms import SignupForm


class UserCreationForm(SignupForm):
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    phone = forms.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = ("email", 'first_name', 'last_name', 'phone', )
    
    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.phone = self.cleaned_data.get('phone')
        user.save()
        return user


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("email",)


class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", 'phone', )
