from datetime import datetime, date, time
from temas import menu_temas

eventos = []
id_evento = 1
def cadastrar_evento():
    from util import limpar_tela
    limpar_tela()
    #add carga horaria
    global id_evento
    nome = input("Nome: ")
    while True:
        try:
            data_evento = input("Data do evento (dd/mm/aaaa): ")
            data = datetime.strptime(data_evento, "%d/%m/%Y").date()
            if data < date.today():
                print("Não é possível cadastrar eventos em datas passadas.")
                continue
            
            print("Digite o horário que o evento irá ocorrer (07:00 - 18:00)")
            hora = input("Digite o horário do evento (h:min): ")
            horario = datetime.strptime(hora, "%H:%M").time()
            horario_inicio = time(7,0)
            horario_fim = time(18,0)
            if horario_inicio > horario and horario > horario_fim:
                print("Horário não comercial. Escolha um horário entre as 07:00 às 18:00.")
                continue
            #posso fazer isso?
            break 
        except ValueError:
            print("Data/hora inválida. Tente novamente.")
    evento = {
        'id' : id_evento,
        'nome' : nome,
        'data_evento' : data,
        'hora_evento' : horario,
        'tema' : menu_temas(),
        'participantes' : []
        
    }
    eventos.append(evento)
    id_evento += 1
    print(f"Evento {evento['nome']} cadastrado com sucesso!")

def exibir_eventos():
    from util import limpar_tela
    limpar_tela()
    #ta mostrando nenhum evento cadastrado e ainda sim mandando digitar o id
    if len(eventos) == 0:
        print("Nenhum evento cadastrado.")
        return

    print("Eventos cadastrados:")
    for event in sorted(eventos, key=lambda e: e['data_evento']):
        print(f"Data: {event['data_evento']} - Hora: {event['hora_evento']}")
        print(f"Código do evento: {event['id']}")
        print(f"Nome: {event['nome']}")
        print(f"Tema: {event['tema']}")
        print("")
        #acho q n precisa de participante aq

def listar_participantes_evento():
    from util import ler_id, existencia, verificar_participantes, limpar_tela
    from participante import participantes
    limpar_tela()
    exibir_eventos()
    print("")
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
    