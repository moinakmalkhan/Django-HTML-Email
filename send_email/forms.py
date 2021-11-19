from django import forms

class EmailForm(forms.Form):
    to_email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=200, required=True)
    html_content = forms.CharField(max_length=500,widget=forms.Textarea(), required=True)
    