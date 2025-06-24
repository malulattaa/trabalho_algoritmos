from util import limpar_tela, ler_id, existencia, verificar_email
from temas import menu_temas
from evento import exibir_eventos
from dados import participantes, id_participante, eventos

def cadastrar_participante():
    """ 
    cadastra novo participante com nome, e-mail e pref temática
    """
    global id_participante
    limpar_tela()
    
    nome = input("Nome completo: ")
    #ver se digitar nome vazio
    email = input("e-mail: ")
    verificar_email(email, participantes)
    
    preferencia = set()
    while True:
        resposta = input("Deseja adicionar preferência temática? (S/N)").upper()
        if resposta == 'S':
            print(f'{"PREFERÊNCIA TEMÁTICA":^40}')
            #da pra chamar um menu geral?
            tema = menu_temas() 
            if tema in preferencia:
                print("Essa preferência já foi adicionada.")
            else:
                preferencia.add(tema)
        elif resposta == 'N':
            break
        else:
            print("Digite S (sim) ou N (não).")
        
    participantes[id_participante] = {
        'nome' : nome,
        'email' : email, #ver se pode por e-mal
        'pref_tematica' : list(preferencia),
        'eventos' : []
    }
    limpar_tela()
    print(f"Participante {nome} cadastrado com sucesso!")
    id_participante += 1
    
def procurar_participante():
    """ 
    busca um participante por id, mostrando suas informações e os eventos em que está inscrito
    """
    id_participante = ler_id("Digite o id do participante que deseja buscar: ")
    participante = existencia(id_participante, participantes)
    if not participante: 
        return
    limpar_tela()
    print(f"{id_participante} - {participante['nome']}")
    print(f"E-mail: {participante['email']}")
    print("")
    print(f"Preferências temáticas: ")
    print(",".join(participante['pref_tematica']) if participante['pref_tematica'] else "O participante não tem preferência temática")
    print("")
    print(f"Eventos que o participante está inscrito: ")
    if participante['eventos']:
        for id_evento in participante['eventos']:
            evento = eventos.get(id_evento)
            print(f"ID: {id_evento} | Nome: {evento['nome']} | Data: {evento['data_evento']} | Horário: {evento['hora_evento']} | Tema: {evento['tema']}")
    else:
        print("O participante não está inscrito em eventos.")
        
def atualizar_email():
    """
    atualiza o e-mail de um participante ja cadastrado
    """
    id_participante = ler_id("Digite o id do participante que deseja alterar o e-mail: ")
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
    """ 
    remove um participante pelo id
    """
    id_participante = ler_id("Digite o id do participante que deseja deletar: ")
    participante = existencia(id_participante, participantes)
    if not participante:
        return
    del participantes[id_participante]
    print(f"Participante {participante['nome']} removido com sucesso.")
    
def inscricao_evento():
    """
    inscrição de participante em um evento com verificação se ele ja esta inscrito
    """
    #se nenhum evento tiver cadastrado ja para
    if not eventos:
        print("Não há eventos disponíveis para realizar inscrição.")
        return
    exibir_eventos()
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
    
#listar todos os eventos em que 1 participante esta inscrito
