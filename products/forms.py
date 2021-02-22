# some of the code was copied from Boutique Ado project's repository
# and modified according to the project's needs
from django import forms
from .widgets import CustomClearableFileInput
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image01 = forms.ImageField(label='Image01', required=True,
                               widget=CustomClearableFileInput)
    image02 = forms.ImageField(label='Image02', required=True,
                               widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'border-black rounded-2'
