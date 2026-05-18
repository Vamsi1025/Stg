from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-amber-500',
        'placeholder': 'Your Name',
    }))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'class': 'w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-amber-500',
        'placeholder': 'Phone Number',
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-amber-500',
        'placeholder': 'How can we help?',
        'rows': 5,
    }))
