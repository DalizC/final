from django.urls import path

from . import views

app_name = 'agenda'
urlpatterns = [
    # ex: /agenda/
    path('', views.especialidades, name='especialidades'),
    path('medicos', views.medicos, name='medicos'),
    path('agendar_hora', views.agendar_hora, name='agendar'),
    # ex: /agenda/login
    # path('login', views.login, name='login'),
    # ex: /agenda/logout
    path('logout', views.logout, name='logout'),
    # ex: /agenda/especialidad/5
    #path('<int:especialidad_id>/', views.medicos, name='medicos'),
    # ex: /agenda/medico/5
    path('medico/<int:medico_id>/', views.medico, name='medico'),
    # ex: /polls/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]
