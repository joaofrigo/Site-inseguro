from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('teste/', teste, name = 'teste'),
    path('', home_view, name='home'),
    path('exemplo/', exemplo_view, name='exemplo'),
    path('contato/', contato_view, name='contato'),
    path('phising/', phising_view, name='phising'),
    path('phising_facebook', phising_facebook_view, name = 'phising_facebook'),
    path('facebook_login/', facebook_login, name='facebook_login'),
    #path('meu_aplicativo/', include('meu_aplicativo.urls')),
    #path('index/', index, name = 'index'),
    #path('charts/', charts, name = 'charts')
    # Outras rotas do projeto aqui...
]
