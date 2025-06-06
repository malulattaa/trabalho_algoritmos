from datetime import datetime


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
        #'tema' : tema
        
    }
    eventos.append(evento)
    #por um print aq de cadastrado com sucesso
    
def exibir_eventos():
    if len(eventos) == 0:
        print("Nenhum evento cadastrado.")
        return

    print("Eventos cadastrados:")
    for event in eventos:
        print(f"Nome: {event['nome']}")
        print(f"Data: {event['data']}")
        print(f"Tema: {event['tema']}")
        #acho q n precisa de participante aq
    
