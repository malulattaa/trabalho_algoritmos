from datetime import datetime
from util import menu_temas


eventos = []
contador_evento = 1
def cadastrar_evento():
    global contador_evento
    nome = input("Nome: ")
    while True:
        data_evento = input("Data do evento (dd/mm/aaaa): ")
        try:
            data = datetime.strptime(data_evento, "%d/%m/%Y").date()
            break 
        except ValueError:
            print("Data inválida. Tente novamente.")
    evento = {
        'id' : contador_evento,
        'nome' : nome,
        'data_evento' : data,
        'tema' : menu_temas()
        
    }
    eventos.append(evento)
    contador_evento += 1
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
    
def inscricao_evento():
    exibir_eventos()
    while True:
        sair = input("Deseja se inscrever em algum evento? S (sim) / N (não) ").upper()
        if sair == 'N':
            break
        elif sair == 'S':
            try:
                codigo = int(input("Digite o código do evento que deseja se inscrever: "))
            except ValueError:
                print("Código inválido. Tente novamente.")
                continue
            filtro = filter(lambda x: x['id'] == codigo, eventos)
            evento_encontrado = next(filtro, None)
            if evento_encontrado:
                print(f"Evento {evento_encontrado['nome']} encontrado")
                try:
                    id_participante = int(input("Digite o ID do participante a ser inscrito: "))
                except ValueError:
                    print("ID inválido.")
                    continue
                pessoa = next((p for p in participantes if p['id'] == id_participante), None)
            else:
                print("Evento não encontrado!")
                    
                
def listar_participantes_evento():
    pass