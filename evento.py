from datetime import datetime
from temas import menu_temas

eventos = []
id_evento = 1
def cadastrar_evento():
    global id_evento
    nome = input("Nome: ")
    while True:
        data_evento = input("Data do evento (dd/mm/aaaa): ")
        try:
            data = datetime.strptime(data_evento, "%d/%m/%Y").date()
            break 
        except ValueError:
            print("Data inválida. Tente novamente.")
    evento = {
        'id' : id_evento,
        'nome' : nome,
        'data_evento' : data,
        'tema' : menu_temas(),
        'participantes' : []
        
    }
    eventos.append(evento)
    id_evento += 1
    print(f"Evento {evento['nome']} cadastrado com sucesso!")

def exibir_eventos():
    if len(eventos) == 0:
        print("Nenhum evento cadastrado.")
        return

    print("Eventos cadastrados:")
    for numero, event in enumerate(eventos, start=1):
        print(f"Evento {numero}")
        print(f"Código do evento: {event['id']}")
        print(f"Nome: {event['nome']}")
        print(f"Data: {event['data_evento']}")
        print(f"Tema: {event['tema']}")
        print("")
        #acho q n precisa de participante aq

def listar_participantes_evento():
    from util import buscar_evento
    from participante import participantes
    exibir_eventos()
    try:
        id_evento = int(input("Digite o ID do evento: "))
    except ValueError:
        print("ID inválido.")
    evento = buscar_evento(id_evento, eventos)
    if not evento:
        print("Evento não encontrado.")
        return
    filtrar = list(filter(lambda p: p['id'] in evento['participantes'], participantes))
    print(f"Participantes inscritos no evento {evento['nome']}")
    print("")
    for p in filtrar:
        print(f"{p['nome']} - {p['email']}")