from django import forms
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class Coordinate_Form(forms.Form):
    x_coordinate = forms.IntegerField()
    y_coordinate = forms.IntegerField()