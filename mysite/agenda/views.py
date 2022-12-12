import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse

from .models import Especialidad, Medico


# @login_required
def especialidades(request):
    especialidades_all_list = Especialidad.objects.order_by('-descripcion')
    medicos_all_list = Medico.objects.all()
    context = {'especialidades_all_list': especialidades_all_list,
               'medicos_all_list': medicos_all_list,
               'medicos_url': reverse('agenda:medicos')
               }
    return render(request, 'agenda/especialidades.html', context)


def getMedicoByEspecialidad(self, *args, **kwargs):
    filter_category = self.request.GET.get("filter_category")
    queryset = Medico.objects.filter(Especialidad=filter_category)
    queryset_filtered = queryset.filter()
    return queryset_filtered


def agendar(request):
    especialidades_all_list = Especialidad.objects.order_by('-descripcion')
    medicos_all_list = Medico.objects.all()
    context = {'especialidades_all_list': especialidades_all_list,
               'medicos_all_list': medicos_all_list}
    return render(request, 'agenda/agendar.html', context)


def medicos(request):
    data = json.loads(request.body)
    medicos = Medico.objects.filter(especialidad__id=data['id'])
    # print(medicos)
    return JsonResponse(list(medicos.values("id", "nombres", "apellidos")), safe=False)


def medico(request, medico_id):
    medico = get_object_or_404(Medico, pk=medico_id)
    return render(request, 'agenda/horas.html', {'medico': medico})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/agenda/')
        else:
            # Return an 'invalid login' error message.
            return HttpResponseRedirect('/agenda/')
    else:
        return render(request, 'agenda/login.html')


""" def login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'form.html', {'form': form}) """


@login_required
def logout(request):
    logout(request)
    # Redirect to a success page.
