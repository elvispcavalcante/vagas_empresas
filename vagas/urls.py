from django.urls import path
from . import views

app_name = 'vagas'

urlpatterns = [
    path('nova_vaga/', views.nova_vaga, name="nova_vaga")
]
