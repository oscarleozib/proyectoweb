from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import FormularioContactos
from django.core.mail import EmailMessage
from misitioweb.settings import EMAIL_HOST_USER
"""
def contact(request):   
    if request.method == 'POST':         #en este caso procesaremos el formulario
        form = FormularioContactos(request.POST)#aquí almacenamos los datos del formulario
        if form.is_valid():#comprobamos que los datos del formulario son válidos
            cd = form.cleaned_data
            #enviaremos el email y redireccionamos
            return redirect(reverse('contact')+'?ok')
    else:
        form = FormularioContactos()
    return render(request, 'contact/contact.html', {'form': form})
"""
def contact(request):
    if request.method == 'POST':
        form = FormularioContactos(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(form.data.values)
            #enviaremos el email y redireccionamos
#AQUÍ INTRODUCIMOS LOS DATOS DEL ENVÍO DEL MAIL
            email = EmailMessage (
                'Nuevo mensaje de MISITIOWEB',
                'De {} <{}>\n\{}'.format(cd['name'], cd['email'], cd['message']), #Cuerpo                
                 EMAIL_HOST_USER, # Origen
                reply_to=[cd['email']])#Destinno # type: ignore)#email de respuesta
#AQUÍ INTRODUCIMOS EL ENVÍO DEL MAIL
            try:
                email.send()
                #si todo va ok, redireccionamos a ?ok
                return redirect(reverse('contact')+'?ok')
            except:
                #si algo falla, redireccionamos a ?fail
                return redirect(reverse('contact')+'?fail')
    else:
        form = FormularioContactos()
    return render(request, 'contact/contact.html', {'form': form})