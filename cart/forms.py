from django import forms

# allowing user to select quantity of an item to order to a limit of 20
ITEM_QUANTITY_CHOICES =[(i, str(i)) for i in range(1, 11)]

class CartAddItemForm(forms.Form):

    # convert input to integer using coerce=int
    quantity = forms.TypedChoiceField(
        choices=ITEM_QUANTITY_CHOICES, coerce=int)

    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

