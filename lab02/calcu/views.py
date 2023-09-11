from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'titulo':"Calcu",
    }
    return render(request, 'calcu/formulario.html',context)

def enviar(request):
    if request.method == 'POST':
        num1 = float(request.POST.get('num1', 0))
        num2 = float(request.POST.get('num2', 0))
        operacion = request.POST.get('operacion', '')

        if operacion == 'suma':
            resultado = num1 + num2
            operacion_texto = 'Suma'
        elif operacion == 'resta':
            resultado = num1 - num2
            operacion_texto = 'Resta'
        elif operacion == 'multiplicacion':
            resultado = num1 * num2
            operacion_texto = 'Multiplicación'
        else:
            resultado = 0
            operacion_texto = 'Operación no válida'

        context = {
            'titulo': "Resultado",
            'operacion': operacion_texto,
            'num1': num1,
            'num2': num2,
            'resultado': resultado,
        }
        return render(request, 'calcu/respuesta.html', context)
    else:
        return HttpResponse("Método no permitido")