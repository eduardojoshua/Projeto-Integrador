from django import forms
from .models import Aluno
from .models import Curso

class AlunoForm(forms.ModelForm):
    data_matricula = forms.DateField(input_formats=['%Y-%m-%d'])
    class Meta:
        model = Aluno
        fields = '__all__'  # Pode ajustar para incluir apenas os campos desejados, se necessário

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'  # Pode ajustar para incluir apenas os campos desejados, se necessário

