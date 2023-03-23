from django.shortcuts import render
from django.http import HttpResponse
from apps.Publigest.models import DataScrapy, EntidadesNombradas, PalabrasClaves, EntidadesNombradas_texto
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
class Home(LoginRequiredMixin, TemplateView):
    template_name ='index.html'
    login_url = 'Publigest:login'

@login_required(login_url="/login/")
def main(request):
    return render(request, 'index.html')
@login_required(login_url="/login/")
def grafic(request):
    return render(request, 'lda.html')
@login_required(login_url="/login/")
def extrac(request):
    data = DataScrapy.objects.all()
    contexto = {'posts': data}
    return render(request, 'posts.html', contexto)
@login_required(login_url="/login/")
def entidades(request):
    data = EntidadesNombradas.objects.all()
    contexto = {'entidades': data}
    return render(request, 'ner.html', contexto)

@login_required(login_url="/login/")
def keyWords(request):
    data = PalabrasClaves.objects.all()
    contexto = {'key': data}
    return render(request, 'claves.html', contexto)

@login_required(login_url="/login/")
def entidades_text(request):
    data = EntidadesNombradas_texto.objects.all()
    contexto = {'entidades_t': data}
    return render(request, 'ner_text.html', contexto)