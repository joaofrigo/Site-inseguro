from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
from user_agents import parse
import requests
import datetime
import json


def home_view(request):
    return render(request, 'home.html')

def exemplo_view(request):
    context = {
        'titulo': 'Este é um Título de Exemplo',
        'mensagem': 'Esta é uma mensagem de exemplo que está sendo passada do contexto do template.',
        'mensagem_2': 'Não tem nada de estranho com essa página, siga em frente...'
    }
    return render(request, 'exemplo.html', context)

def contato_view(request):
    return render(request, 'contato.html')

@csrf_exempt
def log_key(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        keys = data.get('keys')

        # Armazena as teclas pressionadas na sessão
        if 'keys_pressed' not in request.session:
            request.session['keys_pressed'] = ''

        request.session['keys_pressed'] += keys
        request.session.modified = True  # Marca a sessão como modificada

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)

def clickjacking_view(request):
    return render(request, 'clickjacking_home.html')

def clickjacking_1_view(request):
    return render (request, 'clickjacking_1.html')

def clickjacking_2_view(request):
    return render(request, 'clickjacking_2.html')


def phising_view(request):
    return render(request, 'phising_home.html')


def phising_facebook_view(request):
    return render(request, 'phising_facebook.html')

def facebook_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('senha')

        # Adiciona informações de login à sessão
        if 'info_usuario_lista' not in request.session:
            request.session['info_usuario_lista'] = []

        # Constrói um dicionário com as informações de login
        login_info = {
            'session_id': request.session['session_id'],
            'login_email_facebook': email,
            'login_time_facebook': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'login_senha_facebook': password,
        }

        # Adiciona as informações de login à lista na sessão
        request.session['info_usuario_lista'].append(login_info)

        # Salvando a sessão explicitamente (embora o Django geralmente faça isso automaticamente)
        request.session.modified = True

        return render(request, 'home.html')

    

    
def phising_instagram_view(request):
    return render(request, 'phising_instagram.html')

def instagram_login(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')

        # Adiciona informações de login à sessão
        if 'info_usuario_lista' not in request.session:
            request.session['info_usuario_lista'] = []

        # Constrói um dicionário com as informações de login
        login_info = {
            'session_id': request.session['session_id'],
            'login_email_instagram': email,
            'login_time_instagram': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'login_senha_instagram': password,
        }

        # Adiciona as informações de login à lista na sessão
        request.session['info_usuario_lista'].append(login_info)

        # Salvando a sessão explicitamente (embora o Django geralmente faça isso automaticamente)
        request.session.modified = True

        return render(request, 'home.html')



def mostrar_info_usuario(request):
    info_usuario_lista = request.session.get('info_usuario_lista', [])
    keys_pressed = request.session.get('keys_pressed', [])
    print("keys pressed:", keys_pressed)
    
    context = {
        'info_usuario_lista': info_usuario_lista,
        'keys_pressed': keys_pressed,
    }
    
    return render(request, 'mostrar_info_usuario.html', context)

def limpar_sessao(request):
    # Limpa todos os dados da sessão
    request.session.clear()
    return redirect('home')


"""  
def capturar_info_usuario(request):
    # Captura informações básicas do usuário
    ip_address = request.META.get('REMOTE_ADDR')
    user_agent_str = request.META.get('HTTP_USER_AGENT')
    referer = request.META.get('HTTP_REFERER')

    # Analisa o agente do usuário para obter informações detalhadas
    user_agent = parse(user_agent_str)
    browser = user_agent.browser.family
    browser_version = user_agent.browser.version_string
    os = user_agent.os.family
    os_version = user_agent.os.version_string

    # Faz uma requisição para obter informações de geolocalização baseadas no IP
    ipinfo_url = f'http://ipinfo.io/{ip_address}/json'
    response = requests.get(ipinfo_url)
    if response.status_code == 200:
        data = response.json()
        country = data.get('country', '')
        city = data.get('city', '')
        hostname = data.get('hostname', '')
        isp = data.get('org', '')
    else:
        country = city = hostname = isp = 'Informações não disponíveis'

    # Constrói um dicionário com todas as informações coletadas
    info_usuario = {
        'data_hora': request.META.get('REQUEST_TIME'),
        'ip_address': ip_address,
        'country': f"{country}, {city}",
        'browser': f"{browser} ({browser_version})",
        'os': f"{os} {os_version}",
        'user_agent': user_agent_str,
        'referer': referer,
        'hostname': hostname,
        'isp': isp,
    }

"""
"""
def charts(request):
    # Dados de exemplo
    data = {
        'labels': ['A', 'B', 'C', 'D'],
        'datasets': [{
            'label': 'Exemplo',
            'data': [12, 19, 3, 5],
        }]
    }

    chart = BarChart(data)
    return JsonResponse(chart.to_dict())
"""
