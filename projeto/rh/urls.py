from django.urls import include, path

from projeto.rh import views as v





urlpatterns = [
    path('', v.rh, name='cad'),
    path('consulta/', v.consulta, name='consulta'),
    path('detalhe/<int:pk>/', v.detalhe, name='detalhe'),
   
    
]
