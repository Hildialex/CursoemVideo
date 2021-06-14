def acessar(msg):
    import requests
    url = msg
    try:
        if requests.get(url).status_code == 200:
            print('\033[0;32mO site do pudim está disponível!\033[m')
    except:
        print('\033[0;31mO site do pudim não está acessivel!\033[m')
def verificarAcesso(msg):
    import urllib.request
    import json
    try:
        url = urllib.request.urlopen(f'https://{msg}.com')
        x = url.read()
        y = json.loads(x.decode('utf-8'))
        teste = y['valor']
        print(teste)
    except Exception as erro:
        print(f'Servidor indisponível. Erro de {erro}')

acessar("https://youtube.com")
verificarAcesso('youtube')