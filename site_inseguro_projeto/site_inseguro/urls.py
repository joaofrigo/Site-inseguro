from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('teste/', teste, name = 'teste'),
    path('', home_view, name='home'),
    path('exemplo/', exemplo_view, name='exemplo'),
    path('contato/', contato_view, name='contato'),

    path('log_key/', log_key, name='log_key'),

    path('clickjacking/', clickjacking_view, name='clickjacking'),
    path('clickjacking_1/', clickjacking_1_view, name='clickjacking_1'),
    path('clickjacking_2/', clickjacking_2_view, name='clickjacking_2'),

    path('phising/', phising_view, name='phising'),
    path('phising_facebook', phising_facebook_view, name = 'phising_facebook'),
    path('facebook_login/', facebook_login, name='facebook_login'),

    path('phising_instagram/', phising_instagram_view, name='phising_instagram'),
    path('instagram_login/', instagram_login, name='instagram_login'),

    path('mostrar-info-usuario/', mostrar_info_usuario, name='mostrar_info_usuario'),
    path('limpar-sessao/', limpar_sessao, name='limpar_sessao'),
    #path('meu_aplicativo/', include('meu_aplicativo.urls')),
    #path('index/', index, name = 'index'),
    #path('charts/', charts, name = 'charts')
    # Outras rotas do projeto aqui...
]
