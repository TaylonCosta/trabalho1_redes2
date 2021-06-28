import requests

def checatempo():
    print("\nQuestao 2: ")
    conexao = requests.post('http://google.com.br')
    print(conexao.elapsed.total_seconds())