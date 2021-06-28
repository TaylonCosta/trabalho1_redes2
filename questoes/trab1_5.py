from requests import get

def ip_externo():
    print("\nQuestao 5: ")
    ip = get('https://api.ipify.org').text
    print('IP publico: ' + ip)