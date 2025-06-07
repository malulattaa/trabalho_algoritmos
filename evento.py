from datetime import datetime
from util import menu_temas


eventos = []

def cadastrar_evento():
    nome = input("Nome: ")
    while True:
        data_evento = input("Data do evento (dd/mm/aaaa): ")
        try:
            data = datetime.strptime(data_evento, "%d/%m/%Y").date()
            break 
        except ValueError:
            print("Data inválida. Tente novamente.")
            
    #tema = menu_temas
    #participante

    evento = {
        'nome' : nome,
        'data_evento' : data,
        'tema' : menu_temas()
        
    }
    eventos.append(evento)
    print(f"Evento {evento['nome']} cadastrado com sucesso!")

def exibir_eventos():
    if len(eventos) == 0:
        print("Nenhum evento cadastrado.")
        return

    print("Eventos cadastrados:")
    for numero, event in enumerate(eventos, start=1):
        print(f"Evento {numero}")
        print(f"Nome: {event['nome']}")
        print(f"Data: {event['data_evento']}")
        print(f"Tema: {event['tema']}")
        print("")
        #acho q n precisa de participante aq
    
