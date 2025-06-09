from temas import menu_temas
from evento import exibir_eventos

participantes = []

id_participante = 1
def cadastrar_participante():
    from util import limpar_tela
    limpar_tela()
    global id_participante
    nome = input("Nome completo: ")
    #ver se digitar nome vazio
    email = input("e-mail: ")
    
    emails_existentes = set(p['email'] for p in participantes)
    
    if email in emails_existentes:
        print("Esse e-mail já está sendo usado.")
        return
    
    preferencia = []
    while input("Deseja adicionar uma preferência temática? (S para sim)/(N para não): ").upper().strip() == 'S':
        print(f'{"PREFERÊNCIA TEMÁTICA":^40}')
        tema = menu_temas() 
        preferencia.append(tema)
        
    participante = {
        'id': id_participante,
        'nome' : nome,
        'email' : email, #ver se pode por e-mal
        'pref_tematica' : preferencia,
        'eventos' : []
    }
    participantes.append(participante)
    id_participante += 1
    print(f"Participante {nome} cadastrado com sucesso!")
    
def procurar_participante():
    from util import ler_id, existencia
    id_participante = ler_id("Digite o id do participante que deseja buscar: ")
    participante = existencia(id_participante, participantes)
    if not participante: 
        return
    print(f"Participante {participante['id']}:")
    print(f"Nome: {participante['nome']}")
    print(f"E-mail: {participante['email']}")
    print(f"Preferências temáticas: ")
    print(",".join(participante['pref_tematica']) if participante['pref_tematica'] else "O participante não tem preferência temática.")
    print(f"Eventos: ")
    print(",".join(participante['eventos']) if participante['eventos'] else "O participante não está inscrito em eventos.")

def atualizar_email():
    from util import ler_id, existencia
    id_participante = ler_id("Digite o id do participante que deseja buscar: ")
    participante = existencia(id_participante, participantes)
    if not participante:
        return
    print("Participante encontrado: ")
    print(f"Nome: {participante['nome']}")
    print(f"E-mail atual: {participante['email']}")
    print("")
    email_novo = input(f"Digite o novo e-mail do participante {participante['nome']}: ")
    participante['email'] = email_novo
    print(f"O e-mail do participante {participante['nome']} foi alterado com sucesso para {email_novo}.")

def deletar_participante():
    from util import ler_id, existencia
    id_participante = ler_id("Digite o id do participante que deseja buscar: ")
    participante = existencia(id_participante, participantes)
    if not participante:
        return
    participantes.remove(participante)
    print(f"Participante {participante['nome']} removido com sucesso.")
    
def inscricao_evento():
    from util import existencia, ler_id
    from evento import eventos, exibir_eventos
    exibir_eventos()
    #se nenhum evento tiver cadastrado ja para
    
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
    participante['eventos'].append(id_evento)
    evento['participantes'].append(id_participante)
    print(f"{participante['nome']} inscrito no evento {evento['nome']} com sucesso!")