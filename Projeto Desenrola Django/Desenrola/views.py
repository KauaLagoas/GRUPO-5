from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Usuario
from django.contrib import messages
from .models import Denuncia


# CADASTRO: salva um usuário novo no banco
def cadastrarUsuario(request):
    erro = ""
    if request.method == "POST":
        if Usuario.objects.filter(username=request.POST["username"]).exists():
            erro = "Esse usuário já existe"
        else:
            Usuario.objects.create(
                nome=request.POST["nome"],
                username=request.POST["username"],
                senha=make_password(request.POST["password"]),
                habilidadeEnsina=request.POST["ensina"],
                habilidadeAprende=request.POST["aprende"],
            )
            # Cria também o login do Django, com o mesmo username
            user = User(username=request.POST["username"])
            user.set_password(request.POST["password"])
            user.save()
            return redirect("/usuarios/")
    return render(request, "usuarios/cadastro.html", {"erro": erro})


# LISTA: busca todos os usuários no banco
@login_required
def listarUsuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, "usuarios/lista.html", {"usuarios": usuarios})


# EDIÇÃO: mostra os dados atuais e salva as mudanças
@login_required
def editarUsuario(request, idUsuario):
    usuario = get_object_or_404(Usuario, id=idUsuario)
    if request.method == "POST":
        usuario.nome = request.POST["nome"]
        usuario.habilidadeEnsina = request.POST["ensina"]
        usuario.habilidadeAprende = request.POST["aprende"]
        usuario.save()
        return redirect("/usuarios/")
    return render(request, "usuarios/editar.html", {"usuario": usuario})


# REMOÇÃO: apaga o usuário do banco
@login_required
def removerUsuario(request, idUsuario):
    usuario = get_object_or_404(Usuario, id=idUsuario)
    if request.method == "POST":
        User.objects.filter(username=usuario.username).delete()  # apaga também o login
        usuario.delete()
    return redirect("/usuarios/")

def meu_perfil(request):
    return render(request, 'perfil.html')

def editar_perfil(request):
    return render(request, 'editar.html')

def minhas_sessoes(request):
    return render(request, 'sessoes.html')

def erro404(request):
    return render(request, 'erro404.html')

def home(request):
    return render(request, 'home.html')    

def reportar(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        alvo = request.POST.get('alvo')
        motivo = request.POST.get('motivo')
        descricao = request.POST.get('descricao')
        
        Denuncia.objects.create(
            tipo=tipo,
            alvo=alvo,
            motivo=motivo,
            descricao=descricao
        )
        
        messages.success(request, 'Sua denúncia foi registrada com sucesso e será analisada pela equipe.')
        return redirect('reportar')
        
    return render(request, 'denuncia.html')

# PERFIL PÚBLICO
# Dados de EXEMPLO. Quando os models Habilidade e Avaliacao existirem,
# estes dicionários são trocados por consultas ao banco.
PERFIS_EXEMPLO = {
    "marina": {
        "nome": "Marina Costa",
        "iniciais": "MC",
        "cidade": "São Paulo, SP",
        "bio": "Estudante de Design que ama música e artesanato. Topa trocar ideia sobre qualquer coisa criativa!",
        "trocas": 23,
        "habilidades": [
            {"nome": "Fotografia analógica", "categoria": "Artes e Criatividade", "formato": "Presencial"},
            {"nome": "Desenho", "categoria": "Artes e Criatividade", "formato": "Online"},
            {"nome": "Violão", "categoria": "Música", "formato": "Online"},
            {"nome": "Design gráfico", "categoria": "Artes e Criatividade", "formato": "Online"},
        ],
        "avaliacoes": [
            {"autor": "Thiago Mendes", "nota": 5, "habilidade": "Violão", "data": "02/11/2026",
             "texto": "Aula super paciente e bem organizada. Saí tocando minha primeira música."},
            {"autor": "Júlia Ramos", "nota": 5, "habilidade": "Fotografia analógica", "data": "25/10/2026",
             "texto": "Marina explica de um jeito muito claro e ainda trouxe a câmera para eu testar."},
            {"autor": "Carlos Lima", "nota": 4, "habilidade": "Desenho", "data": "10/10/2026",
             "texto": "Ótima troca! Só começamos um pouco atrasados, mas o conteúdo foi excelente."},
        ],
    },
    "thiago": {
        "nome": "Thiago Mendes",
        "iniciais": "TM",
        "cidade": "Rio de Janeiro, RJ",
        "bio": "Professor de inglês nas horas vagas. Quero aprender violão e tocar numa roda de amigos.",
        "trocas": 11,
        "habilidades": [
            {"nome": "Inglês (conversação)", "categoria": "Idiomas", "formato": "Online"},
            {"nome": "Preparação para entrevistas", "categoria": "Desenvolvimento Pessoal", "formato": "Online"},
        ],
        "avaliacoes": [
            {"autor": "Marina Costa", "nota": 5, "habilidade": "Inglês (conversação)", "data": "30/10/2026",
             "texto": "Conversamos o tempo todo em inglês e eu me senti à vontade para errar."},
        ],
    },
}
 
 
def perfil_publico(request, username):
    perfil = PERFIS_EXEMPLO.get(username.lower())
    if perfil is None:
        raise Http404("Perfil não encontrado")
 
    avaliacoes = perfil["avaliacoes"]
    for av in avaliacoes:
        av["estrelas"] = "★" * av["nota"] + "☆" * (5 - av["nota"])
 
    quantidade = len(avaliacoes)
    media = sum(av["nota"] for av in avaliacoes) / quantidade if quantidade else None
 
    contexto = {
        "perfil": perfil,
        "primeiro_nome": perfil["nome"].split()[0],
        "username": username.lower(),
        "avaliacoes": avaliacoes,
        "quantidade": quantidade,
        "media": media,
    }
    return render(request, "perfil_publico.html", contexto)