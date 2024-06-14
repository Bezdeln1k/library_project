from django import forms

class UploadXMLForm(forms.Form):
    file = forms.FileField(label='Выберите XML-файл')
