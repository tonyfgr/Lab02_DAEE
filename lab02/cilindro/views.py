from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'titulo':"Cilindro",
    }
    return render(request, 'cilindro/formulario.html',context)
from django.shortcuts import render
from django.http import HttpResponse

def enviar(request):
    if request.method == 'POST':
        altura = float(request.POST.get('altura', 0))
        diametro = float(request.POST.get('diametro', 0))

        volumen = 3.14159265359 * (diametro / 2) ** 2 * altura

        context = {
            'titulo': "Resultado",
            'altura': altura,
            'diametro': diametro,
            'volumen': volumen,
        }
        return render(request, 'cilindro/respuesta.html', context)
    else:
        return HttpResponse("Método no permitido")
