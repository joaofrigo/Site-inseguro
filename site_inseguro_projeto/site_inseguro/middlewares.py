import requests
from user_agents import parse
import socket
import datetime
from django.utils.deprecation import MiddlewareMixin
import uuid

class CapturaInfoUsuarioMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Verifica se o identificador único já está na sessão, caso contrário, gera um novo
        if 'session_id' not in request.session:
            request.session['session_id'] = str(uuid.uuid4())

        # Captura informações básicas do usuário
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR'))
        user_agent_str = request.META.get('HTTP_USER_AGENT', 'Desconhecido')
        referer = request.META.get('HTTP_REFERER', 'Desconhecido')
        language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'Desconhecido')
        protocol = 'HTTPS' if request.is_secure() else 'HTTP'
        landing_page = request.build_absolute_uri()

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

        # Resolução do hostname (DNS reverso)
        try:
            hostname_resolved = socket.gethostbyaddr(ip_address)[0]
        except socket.herror:
            hostname_resolved = 'Hostname não disponível'

        # Captura a data e hora da requisição
        data_hora = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Constrói um dicionário com todas as informações coletadas
        info_usuario = {
            'session_id': request.session['session_id'],  # Adiciona o UUID da sessão
            'data_hora': data_hora,
            'ip_address': ip_address,
            'country': f"{country}, {city}",
            'browser': f"{browser} ({browser_version})",
            'os': f"{os} {os_version}",
            'user_agent': user_agent_str,
            'referer': referer,
            'language': language,
            'protocol': protocol,
            'landing_page': landing_page,
            'hostname': hostname,
            'hostname_resolved': hostname_resolved,
            'isp': isp,
            'login_email': '.',
            'login_senha': '.',
            'login_time': '.',
        }

        # Inicializa a lista info_usuario_lista na sessão, se ainda não estiver inicializada
        if 'info_usuario_lista' not in request.session:
            request.session['info_usuario_lista'] = []

        # Adiciona o novo info_usuario à lista na sessão
        request.session['info_usuario_lista'].append(info_usuario)

        # Adiciona as informações ao objeto de request para uso imediato
        request.info_usuario = info_usuario

        # Debug: imprime a lista atualizada na sessão
        print("lista atualmente é: ", request.session['info_usuario_lista'])
