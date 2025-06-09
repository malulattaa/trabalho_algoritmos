from datetime import datetime, date
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
            if data < date.today():
                print("Não é possível cadastrar eventos em datas passadas.")
                continue
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
    for event in sorted(eventos, key=lambda e: e['data_evento']):
        print(f"Data: {event['data_evento']}")
        print(f"Código do evento: {event['id']}")
        print(f"Nome: {event['nome']}")
        print(f"Tema: {event['tema']}")
        print("")
        #acho q n precisa de participante aq

def listar_participantes_evento():
    from util import ler_id, existencia, verificar_participantes
    from participante import participantes
    
    exibir_eventos()
    id_evento = ler_id("Digite o ID do evento: ")
    evento = existencia(id_evento, eventos)
    if not evento:
        print("Evento não encontrado.")
        return
    inscritos = verificar_participantes(evento, participantes)
    if inscritos:
        print(f"Participantes inscritos no evento {evento['nome']}: ")
        for p in inscritos:
            print(f"{p['nome']} - {p['email']}")
    else:
        print("Esse evento não possui participantes.")
def deletar_evento():
    from util import ler_id, existencia, verificar_participantes
    from participante import participantes
    
    print("Verifique se há participantes inscritos nesse evento antes de deletá-lo.")
    print("")
    exibir_eventos()
    print("")
    
    id_evento = ler_id("Digite o ID do evento: ")
    evento = existencia(id_evento, eventos)
    if not evento:
        return
    
    inscritos = verificar_participantes(evento, participantes)
    if inscritos:
        print("Delete os participantes do evento antes de excluí-lo.")
        return
    
    eventos.remove(evento)
    print(f"Evento {evento['nome']} removido com sucesso.")
    