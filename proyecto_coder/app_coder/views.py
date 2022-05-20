from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Curso
from django.template import loader
# Create your views here.



def cursos(request):

    cursos = Curso.objects.all()
    dicc = {'cursos': cursos}
    plantilla = loader.get_template('plantilla.html')
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def alta_curso(request,nombre):

    curso = Curso(nombre= nombre,camada = 2345)
    curso.save()
    texto = f'Se guardo en la base de datos Curso: {curso.nombre}, Camada: {curso.camada}'
    return HttpResponse(texto)


