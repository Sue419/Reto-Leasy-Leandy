from django import forms

class ReportForm(forms.Form):
    columns = forms.MultipleChoiceField(
        choices=[
            ('nombre', 'Nombre'),
            ('apellidos', 'Apellidos'),
            ('numero de documento', 'Número de documento'),
            ('inicio de contrato', 'Inicio de contrato'),
            ('cuota semanal', 'Cuota semanal'),
            ('marca del auto', 'Marca del auto'),
            ('modelo del auto', 'Modelo del auto'),
            ('placa del auto', 'Placa del auto'),
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
