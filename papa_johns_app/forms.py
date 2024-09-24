from django import forms


class PizzaOrderForm(forms.Form):
    CHOICES = [
        ('margherita', 'Margherita'),
        ('pepperoni', 'Pepperoni'),
        ('vegetarian', 'Vegetarian'),
        ('hawaiian', 'Hawaiian'),
    ]

    pizza_type = forms.ChoiceField(choices=CHOICES)
    comments = forms.CharField(widget=forms.Textarea, required=False)