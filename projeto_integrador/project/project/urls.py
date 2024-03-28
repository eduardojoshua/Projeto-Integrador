from django.contrib.auth import views as auth_views
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('adicionar_aluno/', views.adicionar_aluno, name='adicionar_aluno'),
    path('listar_alunos/', views.listar_alunos, name='listar_alunos'),
]

