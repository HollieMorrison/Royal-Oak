from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["table", "date", "time", "party_size"]
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RoyalOakUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
