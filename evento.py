from datetime import datetime, date, time
from util import limpar_tela, tratar_data, ler_id, existencia, verificar_participantes, menu_geral
from temas import menu_temas
from dados import participantes, eventos, id_evento

def mostrar_evento(id, evento):
    """ exibe as informações de um evento específico """
    print(f"Data: {evento['data_evento'].strftime('%d/%m/%Y')} - Hora: {evento['hora_evento']}")
    print(f"Código do evento: {id}")
    print(f"Nome: {evento['nome']}")
    print(f"Tema: {evento['tema']}")
    print("")
        
def cadastrar_evento():
    """ cadastro de um novo evento com nome, data, horário e tema """
    global id_evento
    limpar_tela()
    nomes_existentes = set(e['nome'] for e in eventos.values())
    while True: 
        nome = input("Nome: ")
        if nome in nomes_existentes:
            print("Esse evento já foi cadastrado. Digite outro nome.")
        else:
            break
        
    while True:
        data = tratar_data()
        if data < date.today():
            print("Não é possível cadastrar eventos em datas passadas.")
            continue
        break
        
    while True:
        print("Digite o horário que o evento irá ocorrer (07:00 - 18:00)")
        hora = input("Digite o horário do evento (h:min): ")    
        try:
            horario = datetime.strptime(hora, "%H:%M").time()
            if horario < time(7,0) or horario > time(18, 0):
                print("Horário não comercial.")
                limpar_tela()
                continue
            break 
        except ValueError:
            print("Hora inválida. Tente novamente.")
            
    eventos[id_evento] = {
        'nome' : nome,
        'data_evento' : data,
        'hora_evento' : horario,
        'tema' : menu_temas(),
        'participantes' : []
        
    }
    print(f"Evento {eventos[id_evento]['nome']} cadastrado com sucesso!")
    id_evento += 1
    limpar_tela()

def exibir_eventos():
    """ exibe os eventos cadastrados, ordenando-os por data crescente """
    limpar_tela()
    
    #ta mostrando nenhum evento cadastrado e ainda sim mandando digitar o id
    # porque algumas outras funções chamam o exibir_eventos() antes de pedir ID, mas essa função em si só exibe.
    if len(eventos) == 0:
        print("Nenhum evento cadastrado.")
        return

    print("Eventos cadastrados:")    
    for id, evento in sorted(eventos.items(), key=lambda e: e[1]['data_evento']):
        mostrar_evento(id, evento)
        #aqui, evento.items() é uma tupla (id, dados_do_evento) onde dados_do_evento é um dicionario
        #e pega a data do evento do indice 1 da tupla que é dicio de evento
    
        #acho q n precisa de participante aq

def listar_participantes_evento():
    """lista os participantes inscritos em um evento específico"""
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
            print(f"ID: {id} - {p['nome']}: {p['email']}")
    else:
        print("Esse evento não possui participantes.")
        
def deletar_evento():
    """ remove o evento se não tiver nenhum particpante inscrito"""
    print("Verifique se há participantes inscritos nesse evento antes de deletá-lo.")
    print("")
    exibir_eventos()
    print("")
    id_evento = ler_id("Digite o ID do evento: ")
    evento = existencia(id_evento, eventos)
    if not evento:
        return
    if verificar_participantes(evento, participantes):
        print("Delete os participantes do evento antes de excluí-lo.")
        return
    del eventos[id_evento]
    print(f"Evento {evento['nome']} removido com sucesso.")
    
def filtrar_evento():
    """ filtra eventos por data ou tema """
    print("Deseja filtrar o evento por tema ou data? ")

    def exibir_filtrados(filtrado):
        limpar_tela()
        if filtrado:
            for id_evento, evento in filtrado:
                mostrar_evento(id_evento, evento)
        else:
            print("Nenhum evento encontrado. ")
            
    def filtrar_tema():
        tema = menu_temas()
        exibir_filtrados(list(filter(lambda item: item[1]['tema'] == tema, eventos.items())))
        
    def filtrar_data():
        data = tratar_data()
        exibir_filtrados(list(filter(lambda item: item[1]['data_evento'] == data, eventos.items())))
        #nao ta pegando
    opcoes = {
        1: ("Tema", filtrar_tema),
        2: ("Data", filtrar_data),
    }
    menu_geral("FILTRAR EVENTO", opcoes)