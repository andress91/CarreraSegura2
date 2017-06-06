from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import RegModelForm, ContactForm
from .models import Registrado
# Create your views here.
def inicio(request):
	titulo="HOLA"
	if request.user.is_authenticated():
		titulo = "Bienvenido %s" %(request.user)
	form=RegModelForm(request.POST or None)
	if form.is_valid():
		form_data= form.cleaned_data
		abc= form_data.get("email")
		abc2= form_data.get("nombre")
		obj= Registrado.objects.create(email=abc,nombre=abc2)
	contex ={
		"titulo":titulo,
		"el_form": form
	}
	return render(request,"inicio.html",contex)
def contact(request):
	titulo = "Contactanos"
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key, value in form.cleaned_data.iteritems():
		# 	print key, value
		# for key in form.cleaned_data:
		# 	print key
		# 	print form.cleaned_data.get(key)
		form_email = form.cleaned_data.get("email")
		form_mensaje = form.cleaned_data.get("mensaje")
		form_nombre = form.cleaned_data.get("nombre")
		asunto = 'Form de Contacto'
		email_from = settings.EMAIL_HOST_USER
		email_to = [email_from,form_email]
		email_mensaje = "%s: %s enviado por %s" %(form_nombre, form_mensaje, form_email)
		send_mail(asunto, 
			email_mensaje,
			email_from,
			email_to,
			fail_silently=False
			)

		# print email, mensaje, nombre
	context = {
		"form": form,
		"titulo": titulo,
	}
	return render(request, "forms.html", context)
def index2(request):

	return render(request,"index2.html",{})
