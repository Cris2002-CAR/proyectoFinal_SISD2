from django import forms

class UploadSQLFileForm(forms.Form):
    file = forms.FileField()
