from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'email', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'name': 'name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address', 'name': 'email'}),
            'body': forms.Textarea(attrs={'name': 'review', 'placeholder': 'Your Review'})
        }




