from util import limpar_tela, ler_id, existencia, tratar_email, titulos
from temas import menu_temas
from dados import participantes, id_participante, eventos
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from evento import exibir_eventos

def cadastrar_participante():
    """ 
    cadastra novo participante com nome, e-mail e pref temática
    """
    global id_participante
    #global permite que eu altere uma variável que foi declarada fora da função
    limpar_tela()
    
    titulos("CADASTRO DE PARTICIPANTE")
    
    nome = input("Nome completo: ")
    email = tratar_email()
    
    preferencia = set()
    while True:
        resposta = input("Deseja adicionar preferência temática? (S/N)").upper()
        if resposta == 'S':
            print("")
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
    print(f"ID: {id_participante} | E-mail: {email}")
    id_participante += 1
    
def procurar_participante():
    """ 
    busca um participante por id, mostrando suas informações e os eventos em que está inscrito
    """
    limpar_tela()
    titulos("CONSULTA DE PARTICIPANTE POR ID")
    listar_participantes()
    id_participante = ler_id("Digite o id do participante que deseja buscar: ")
    participante = existencia(id_participante, participantes)
    if not participante: 
        return
    limpar_tela()
    print(f"{id_participante} | {participante['nome']}")
    print(f"E-mail: {participante['email']}")
    print("")
    print(f"Preferências temáticas: ")
    print(", ".join(participante['pref_tematica']) if participante['pref_tematica'] else "O participante não tem preferência temática")
    print("")
    print(f"Eventos inscritoS: ")
    if participante['eventos']:
        for id_evento in participante['eventos']:
            evento = eventos.get(id_evento)
            print(f"ID: {id_evento} | Nome: {evento['nome']} | Data: {evento['data_evento'].strftime('%d/%m/%Y')} | Horário: {evento['hora_evento']} | Tema: {evento['tema']}")
    else:
        print("O participante não está inscrito em eventos.")
        
def atualizar_email():
    """
    atualiza o e-mail de um participante ja cadastrado
    """
    limpar_tela()
    titulos("ATUALIZAÇÃO DE E-MAIL")
    listar_participantes()
    id_participante = ler_id("Digite o id do participante que deseja alterar o e-mail: ")
    participante = existencia(id_participante, participantes)
    if not participante:
        return
    print("Participante encontrado: ")
    print(f"Nome: {participante['nome']}")
    print(f"E-mail atual: {participante['email']}")
    print("")
    email_novo = tratar_email()
    participante['email'] = email_novo
    print(f"O e-mail do participante {participante['nome']} foi alterado com sucesso para {email_novo}.")

def deletar_participante():
    """ 
    remove um participante pelo id
    """
    limpar_tela()
    titulos("REMOÇÃO DE PARTICIPANTE")
    listar_participantes()
    id_participante = ler_id("Digite o id do participante que deseja deletar: ")
    participante = existencia(id_participante, participantes)
    if not participante:
        return
    del participantes[id_participante]
    # for id_evento in participante['eventos']:
    #     eventos[id_evento]['participantes'].remove(id_participante)
        
    print(f"Participante {participante['nome']} removido com sucesso.")
    
def inscricao_evento():
    """
    inscrição de participante em um evento com verificação se ele ja esta inscrito
    """
    from evento import exibir_eventos
    limpar_tela()
    titulos("INSCRIÇÃO EM EVENTOS")
    if not eventos:
        print("Não há eventos disponíveis para realizar inscrição.")
        return
    exibir_eventos()
    print("")
    listar_participantes()
    id_evento = ler_id("Digite o ID do evento: ")
    evento = existencia(id_evento, eventos)
    if not evento:
        return
    
    id_participante = ler_id("Digite o ID do participante: ")
    participante = existencia(id_participante, participantes)
    if not participante:
        return
    
    # Verifica se o participante já está inscrito no evento.
    if id_evento in participante['eventos']:
        print("O participante já está inscrito nesse evento!")
        return
    
    # o evento é adicionado à lista de eventos do participante
    participante['eventos'].append(id_evento)
    # o participante é adicionado à lista de participantes do evento
    evento['participantes'].append(id_participante)
    print(f"{participante['nome']} inscrito no evento {evento['nome']} com sucesso!")
    
#listar todos os eventos em que 1 participante esta inscrito

def listar_participantes():
    """Lista todos os participantes cadastrados no sistema"""
    titulos("LISTA DE PARTICPANTES")

    if not participantes:
        print("Nenhum participante cadastrado.")
        return

    for id_part, dados in participantes.items():
        print(f"ID: {id_part} | Nome: {dados['nome']} | E-mail: {dados['email']}")
    print()
