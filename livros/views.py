from django.shortcuts import render,redirect
from django.conf import settings
from django.http import HttpResponse
import requests


def index(request):
    response = requests.get('https://hutl.pythonanywhere.com/livros/')
    livros = response.json()
    context = {
        'livros':livros
    }
    return render(request, 'index.html', context)

def adicionar(request):
    if request.method == "POST":
        dados = request.POST
        imagem = request.FILES["imagem"]
        novo_livro = {
            "titulo": dados["titulo"],
            "autor": dados["autor"],
            "ano_lancamento": dados["ano_lancamento"],
            "estado": dados["estado"],
            "paginas": dados["paginas"],
            "editora": dados["editora"],
        }   
        files = {
            "imagem": (imagem.name, imagem, imagem.content_type)
        }
        post_response = requests.post('https://hutl.pythonanywhere.com/livros/', data=novo_livro, files=files)
        return redirect('index')
    
    context = {

    }
    return render(request, 'adicionar.html', context)

def editar(request, id_livro):
    if request.method == "POST":
        dados = request.POST
        imagem = request.FILES.get("imagem")
        novo_livro = {}

        if dados.get("titulo"):
            novo_livro["titulo"] = dados.get("titulo")
        if dados.get("autor"):
            novo_livro["autor"] = dados.get("autor")
        if dados.get("ano_lancamento"):
            novo_livro["ano_lancamento"] = dados.get("ano_lancamento")
        if dados.get("estado"):
            novo_livro["estado"] = dados.get("estado")
        if dados.get("paginas"):
            novo_livro["paginas"] = dados.get("paginas")
        if dados.get("editora"):
            novo_livro["editora"] = dados.get("editora")

        files = {}
        if imagem:
            files["imagem"] = (imagem.name, imagem, imagem.content_type)

        patch_response = requests.patch(f'https://hutl.pythonanywhere.com/livros/{id_livro}/', data=novo_livro, files=files)
        return redirect('index')
    
    context = {}
    return render(request, 'editar.html', context)



def excluir(request, id_livro):
    delete_response = requests.delete(f'https://hutl.pythonanywhere.com/livros/{id_livro}/')
    return redirect('index')
    


