from datetime import datetime
from django.utils import timezone
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import Aluno, Curso
from .forms import CursoForm
from .forms import AlunoForm
from .decorators import superuser_required
import requests

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Usando a função login corretamente
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')

    return render(request, 'login.html')

@superuser_required
def logout(request):
    logout(request)
    # Redireciona para a página após o logout
    return redirect('login')

@superuser_required
def dashboard(request):
    return render(request, 'dashboard.html')

@superuser_required
def adicionar_aluno(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        numero_matricula = request.POST.get('numero_matricula', 0)
        curso_id = request.POST['curso']  # Supondo que o ID do curso seja enviado pelo formulário
        email = request.POST['email']
        endereco= request.POST['endereco']
        telefone = request.POST['telefone']
        estado_id = request.POST['estado']  # Capturar o ID do estado enviado pelo formulário
        cidade_id = request.POST['cidade']  # Capturar o ID da cidade enviado pelo formulário

        # Obter os nomes das cidades e estados da API do IBGE
        estado_nome = obter_nome_estado(estado_id)
        cidade_nome = obter_nome_cidade(cidade_id)

        # Obter o objeto Curso com base no ID selecionado
        curso = Curso.objects.get(pk=curso_id)

        # Capturar a data e hora atual usando timezone.now() do Django
        data_hora_atual = timezone.now().date()
        
        # Formatando a data no formato DD/MM/AAAA em português brasileiro
        data_formatada = data_hora_atual.strftime('%d/%m/%Y')


        # Criar e salvar o objeto Aluno com os dados recebidos e a data/hora atual
        aluno = Aluno(nome=nome, numero_matricula=numero_matricula, curso=curso, email=email, data_matricula=data_formatada, telefone=telefone, estado=estado_nome, cidade=cidade_nome, endereco=endereco)
        aluno.save()

        # Redirecionar para uma página de sucesso ou outra view após adicionar o aluno
        return redirect('listar_alunos')

    # Se não for um método POST, renderizar o formulário vazio
    cursos = Curso.objects.all()
    return render(request, 'adicionar_aluno.html', {'cursos': cursos})

    # Função para obter o nome do estado a partir do ID usando a API do IBGE
def obter_nome_estado(estado_id):
    response = requests.get(f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{estado_id}')
    if response.status_code == 200:
        estado = response.json()
        return estado['nome']
    else:
        return 'Estado Desconhecido'

# Função para obter o nome da cidade a partir do ID usando a API do IBGE
def obter_nome_cidade(cidade_id):
    response = requests.get(f'https://servicodados.ibge.gov.br/api/v1/localidades/municipios/{cidade_id}')
    if response.status_code == 200:
        cidade = response.json()
        return cidade['nome']
    else:
        return 'Cidade Desconhecida'

@superuser_required
def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'listar_alunos.html', {'alunos': alunos})



