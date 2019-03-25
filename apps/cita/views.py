from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import *
from .forms import *
from django.template import RequestContext
from django.db.models.functions import TruncMonth
from django.db.models import Q, Sum, Count

# Create your views here.
#Test
def inicio(request):
    contacto = False
    if request.method == 'POST':
        contacto = True
    return render(request, 'index.html', {'contacto':contacto})

def panel(request):
    return render(request, 'clinica/panel.html', {})

def documentacion(request):
    return render(request, 'documentacion.html', {})

def faq(request):
    return render(request, 'faq.html', {})

def lista_citas(request):
	usuario = request.user
	citas = Cita.objects.select_related("usuario").filter(usuario=usuario).all()
	return render(request, 'clinica/lista_citas.html', {"lista_citas":citas})

def agregar_cita(request):
	usuario = request.user
	if request.method == 'POST':
		cita_form = CitaAgregarForm(request.POST)
		if cita_form.is_valid() :
			cita_form = cita_form.save(commit=False)
			cita_form.usuario = usuario
			cita_form.save()
			messages.success(request, 'La cita se agrego correctamente', extra_tags='safe' )
			return HttpResponseRedirect( reverse_lazy('lista_citas') )
		else:
			return HttpResponseRedirect( reverse_lazy('lista_citas') )
	else:
		cita_form = CitaAgregarForm()
	return render(request, 'clinica/agregar_cita.html', {'cita_form':cita_form, 'titulo':"Agregar Cita"})

def editar_cita(request, id_cita):    
    usuario = request.user
    cita_instance = get_object_or_404(Cita, id=id_cita, usuario=usuario)
    if request.method == 'POST':
        cita_form = CitaEditarForm(request.POST, instance=cita_instance,  usuario=usuario)
        if cita_form.is_valid():
            cita = cita_form.save(commit=False)
            cita.save()
            messages.success(request, 'La cita se edito correctamente', extra_tags='safe' )
            return HttpResponseRedirect( reverse_lazy('lista_citas') )
        else:
            return HttpResponseRedirect( reverse_lazy('lista_citas') )
    else:
        cita_form = CitaEditarForm(instance=cita_instance, usuario=usuario)
    return render(request, 'clinica/agregar_cita.html', {'cita_form':cita_form, 'titulo':"Editar Cita"})


def eliminar_cita(request, id_cita):
    usuario = request.user
    cita = get_object_or_404(Cita, id=id_cita, usuario=usuario)
    url_regreso = reverse_lazy('lista_citas')
    #se obtienen todos los objetos relacionados a eliminar
    deletable_objects, model_count, protected = get_deleted_objects([cita])
    titulo = "Eliminar Cita #{0}".format(id_cita)
    if request.method == 'POST':
        cita.delete()
        messages.success(request, 'Se elimino correctamente la cita #{0}'.format(id_cita), extra_tags='safe' )
        return HttpResponseRedirect(url_regreso)

    return render(request, 'clinica/eliminar_objeto_view.html', {"titulo":titulo, "url_regreso": url_regreso, "deletable_objects": deletable_objects, 'model_count':dict(model_count).items(),'protected':protected } )


from django.contrib.admin.utils import NestedObjects
from django.utils.text import capfirst
from django.utils.encoding import force_text
def get_deleted_objects(objs):
    #basado en http://stackoverflow.com/questions/12158714/how-to-show-related-items-using-deleteview-in-django#
    collector = NestedObjects(using='default')
    collector.collect(objs)
    #
    def format_callback(obj):
        opts = obj._meta
        no_edit_link = '%s: %s' % (capfirst(opts.verbose_name),
                                   force_text(obj))
        return no_edit_link
    #
    to_delete = collector.nested(format_callback)
    protected = [format_callback(obj) for obj in collector.protected]
    model_count = {model._meta.verbose_name_plural: len(objs) for model, objs in collector.model_objs.items()}
    #
    return to_delete, model_count, protected