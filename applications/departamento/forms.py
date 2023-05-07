from django import forms

class NewDepartamentoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellidos = forms.CharField(max_length=50, required=True)
    departamento = forms.CharField(max_length=50)
    shor_name = forms.CharField(max_length=20)
