from datetime import datetime, date, time
from util import limpar_tela, tratar_data, ler_id, existencia, verificar_participantes, menu_geral


id_evento = 1
eventos = {}
def cadastrar_evento():
    
    from temas import menu_temas
    global id_evento
    
    limpar_tela()
    #add carga horaria
    
    nome = input("Nome: ")
    
    while True:
        data = tratar_data()
        if data < date.today():
            print("Não é possível cadastrar eventos em datas passadas.")
            continue
        
        print("Digite o horário que o evento irá ocorrer (07:00 - 18:00)")
        hora = input("Digite o horário do evento (h:min): ")
        
        try:
            horario = datetime.strptime(hora, "%H:%M").time()
            
            horario_inicio = time(7,0)
            horario_fim = time(18,0)
            
            if horario_inicio <= horario <= horario_fim:
                print("Horário não comercial. Escolha um horário entre as 07:00 às 18:00.")
                continue
            #arrumar isso aq pq eu coloquei 06:00 e ele validou
            #posso fazer isso?
            break 
        except ValueError:
            print("Data/hora inválida. Tente novamente.")
        
    eventos[id_evento] = {
        'nome' : nome,
        'data_evento' : data,
        'hora_evento' : horario,
        'tema' : menu_temas(),
        'participantes' : []
        
    }
    print(f"Evento {eventos[id_evento]['nome']} cadastrado com sucesso!")
    id_evento += 1

def exibir_eventos():
    limpar_tela()
    
    #ta mostrando nenhum evento cadastrado e ainda sim mandando digitar o id
    # porque algumas outras funções chamam o exibir_eventos() antes de pedir ID, mas essa função em si só exibe.
    if len(eventos) == 0:
        print("Nenhum evento cadastrado.")
        return

    print("Eventos cadastrados:")
    
    for id, event in sorted(eventos.items(), key=lambda e: e[1]['data_evento']):
        #aqui, evento.items() é uma tupla (id, dados_do_evento) onde dados_do_evento é um dicionario
        #e pega a data do evento do indice 1 da tupla que é dicio de evento
        
        print(f"Data: {event['data_evento']} - Hora: {event['hora_evento']}")
        print(f"Código do evento: {id}")
        print(f"Nome: {event['nome']}")
        print(f"Tema: {event['tema']}")
        print("")
        #acho q n precisa de participante aq

def listar_participantes_evento():
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
        for id, p in inscritos.items():
            print(f"(ID: {id}) - {p['nome']}: {p['email']}")
    else:
        print("Esse evento não possui participantes.")
def deletar_evento():
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
    
    del eventos[id_evento]
    print(f"Evento {evento['nome']} removido com sucesso.")
    
def filtrar_evento():
    from temas import menu_temas
    print("Deseja filtrar o evento por tema ou data? ")

    def exibir_filtrados(filtrado):
        if not filtrado:
            print(f"Nenhum evento encontrado. ")
            return
        for evento in filtrado:
            id_evento = [id for id, e in eventos.items() if e==evento[0]]
            print(f"ID: {id_evento} - {evento['nome']}")
            print(f"{evento['data_evento']} - {evento['hora_evento']}")
            print(f"Tema: {evento['tema']}")
    def filtrar_tema():
        tema = menu_temas()
        exibir_filtrados(list(filter(lambda x: x['tema'] == tema, eventos.values())))
    def filtrar_data():
        data = tratar_data()
        exibir_filtrados(list(filter(lambda x: x['data_evento'] == data, eventos.values())))
    opcoes = {
        1: ("Tema", filtrar_tema),
        2: ("Data", filtrar_data),
    }
    menu_geral(f'{"FILTRAR EVENTO":^40}', opcoes)