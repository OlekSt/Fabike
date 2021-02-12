from django import forms
from .models import Event
import datetime

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'

    date = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y',
        attrs={'placeholder':'e.g. 12/10/2021'}),
        input_formats=('%d/%m/%Y', ),
        )

    time = forms.TimeField(
        widget=forms.TimeInput(format='%H:%M',
        attrs={'placeholder':'e.g. 14:00'}),
        input_formats=('%H:%M', )
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'border-black rounded-2'

        self.fields['date'].required = True
        self.fields['time'].required = True

        
