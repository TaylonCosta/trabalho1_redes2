import socket

def ip_info():
    print("\nQuestao 3: ")
    host = socket.gethostname()
    ip = socket.gethostbyname(host)

    print("host: " + host + "\nIP: " + ip)
