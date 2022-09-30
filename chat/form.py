from django import forms

from .models import Room


class RoomForm(forms.ModelForm):
    الاسم = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "دخل اسمك باش تكمل معانا"})
    )

    class Meta:
        model = Room
        fields = [
            'الاسم',
        ]
