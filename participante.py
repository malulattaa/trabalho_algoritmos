from util import limpar_tela, ler_id, existencia, verificar_email
from temas import menu_temas
from evento import eventos, exibir_eventos

participantes = {}
id_participante = 1
def cadastrar_participante():
    global id_participante
    limpar_tela()
    nome = input("Nome completo: ")
    #ver se digitar nome vazio
    email = input("e-mail: ")
    
    verificar_email(email, participantes)
    
    preferencia = []
    while input("Deseja adicionar uma preferência temática? (S para sim)/(N para não): ").upper().strip() == 'S':
        #se eu digitar qlq outra coisa sem ser s ele leva como n
        print(f'{"PREFERÊNCIA TEMÁTICA":^40}')
        tema = menu_temas() 
        preferencia.append(tema)
        
    participantes[id_participante] = {
        'nome' : nome,
        'email' : email, #ver se pode por e-mal
        'pref_tematica' : preferencia,
        'eventos' : []
    }
    id_participante += 1
    print(f"Participante {nome} cadastrado com sucesso!")
    
def procurar_participante():
    id_participante = ler_id("Digite o id do participante que deseja buscar: ")
    participante = existencia(id_participante, participantes)
    if not participante: 
        return
    print(f"Participante {id_participante}:")
    print(f"Nome: {participante['nome']}")
    print(f"E-mail: {participante['email']}")
    print(f"Preferências temáticas: ")
    print(",".join(participante['pref_tematica']) if participante['pref_tematica'] else "O participante não tem preferência temática")
    print(f"Eventos: ")
    if participante['eventos']:
        print(",".join(eventos[id]['nome'] for id in participante['eventos'] if id in eventos))
    else:
        print("O participante não está inscrito em eventos.")
        
def atualizar_email():
    id_participante = ler_id("Digite o id do participante que deseja buscar: ")
    participante = existencia(id_participante, participantes)
    if not participante:
        return
    print("Participante encontrado: ")
    print(f"Nome: {participante['nome']}")
    print(f"E-mail atual: {participante['email']}")
    print("")
    email_novo = input(f"Digite o novo e-mail do participante {participante['nome']}: ")
    verificar_email(email_novo, participantes)
    participante['email'] = email_novo
    print(f"O e-mail do participante {participante['nome']} foi alterado com sucesso para {email_novo}.")

def deletar_participante():
    id_participante = ler_id("Digite o id do participante que deseja deletar: ")
    participante = existencia(id_participante, participantes)
    if not participante:
        return
    del participantes[id_participante]
    print(f"Participante {participante['nome']} removido com sucesso.")
    
def inscricao_evento():
    
    exibir_eventos()
    #se nenhum evento tiver cadastrado ja para
    #mostrar id e nome do pas participantes
    id_evento = ler_id("Digite o ID do evento: ")
    evento = existencia(id_evento, eventos)
    if not evento:
        return
    
    id_participante = ler_id("Digite o ID do participante: ")
    participante = existencia(id_participante, participantes)
    if not participante:
        return
    if id_evento in participante['eventos']:
        print("O participante já está inscrito nesse evento!")
        return
    participante['eventos'].append(evento['nome'])
    evento['participantes'].append(id_participante)
    print(f"{participante['nome']} inscrito no evento {evento['nome']} com sucesso!")