from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone

from .models import Booking, Table


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["table", "date", "time", "party_size"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.TimeInput(attrs={"type": "time"}),
            "party_size": forms.NumberInput(attrs={"min": 1, "max": 8}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["table"].queryset = Table.objects.all()
        self.fields["table"].empty_label = "Select a table"

    def clean_date(self):
        date = self.cleaned_data["date"]
        if date < timezone.localdate():
            raise forms.ValidationError("Cannot book in the past.")
        return date

    def clean_party_size(self):
        size = self.cleaned_data["party_size"]
        if size < 1 or size > 8:
            raise forms.ValidationError("Party size must be between 1 and 8.")
        return size

    def clean(self):
        cleaned_data = super().clean()
        table = cleaned_data.get("table")
        party_size = cleaned_data.get("party_size")

        if table and party_size and party_size > table.seats:
            self.add_error("party_size", "Too many guests for this table.")

        return cleaned_data


class RoyalOakUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
