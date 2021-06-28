import urllib.request

def checa_conexao():
    print("\nQuestao 1: ")
    try:
        urllib.request.urlopen('http://google.com')
        print("Conectado a intetnet!")
    except:
        print("Sem acesso internet!")

