from django import forms


class ContactForm(forms.Form):
    """
    A form for contact page
    """
    name = forms.CharField(label="Name")
    email = forms.EmailField(label="Email")
    subject = forms.EmailField(label="Subject")
    message = forms.CharField(label="Message",
                                widget=forms.Textarea(attrs={
                                "rows": 10,
                                })
                            )

    class Meta:
        fields = ['name', 'email', 'subject', 'message']
