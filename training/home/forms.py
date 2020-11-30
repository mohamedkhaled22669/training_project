from django import forms

class AddNode(forms.Form):
    subject = forms.CharField(max_length=80)
    content = forms.CharField(max_length=250)
    
    
class UpdateNode(forms.Form):
    id = forms.CharField()
    subject = forms.CharField(max_length=80)
    content = forms.CharField(max_length=250)
    
class DeleteNode(forms.Form):
    id = forms.CharField()


class SendNode(forms.Form):
    id = forms.CharField()
    subject = forms.CharField(max_length=80)
    content = forms.CharField(max_length=250)
    emails = forms.CharField()