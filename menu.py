from util import ler_opcao, limpar_tela, menu_geral
from participante import cadastrar_participante, procurar_participante, atualizar_email, deletar_participante
from estatisticas import estatisticas
from evento import cadastrar_evento, exibir_eventos, listar_participantes_evento, deletar_evento
from temas import trocar_tema

def menu_principal():
    opcoes = {
        1: ("Gerenciar participantes", menu_participantes),
        2: ("Gerenciar eventos", menu_eventos),
        3: ("Estastísticas e relatórios", estatisticas),
    }
    menu_geral(f'{"MENU":^40}', opcoes)

def menu_temas():
    #limpar
    temas = ["Inteligência Artificial", "Web", "Segurança", "Rede", "Programação", "Banco de dados", "Mobile", "Computação em Nuvem", "Robótica"]
    print("_" * 15, "TEMAS", "_" * 15)
    print("1 - Inteligência Artificial - IA")
    print("2 - Web")
    print("3 - Segurança")
    print("4 - Redes")
    print("5 - Programação")
    print("6 - Banco de Dados")
    print("7 - Mobile")
    print("8 - Computação em Nuvem")
    print("9 - Robótica")
    op = ler_opcao(len(temas))
    return temas[op - 1]
    
def menu_eventos():
    #limpar
    opcoes = {
        1: ("Cadastrar novo evento", cadastrar_evento),
        2: ("Exibir lista de eventos", exibir_eventos),
        3: ("Listar participantes por evento", listar_participantes_evento),
        4: ("Remover evento", deletar_evento),
        5: ("Trocar tema de um evento", trocar_tema),
        #6: ("Filtrar evento por tema/data", cadastrar_evento),
        #7: ("Agrupar por tema", cadastrar_evento),
    }
    menu_geral(f'{"EVENTO":^40}', opcoes)
def menu_participantes():
    opcoes = {
        1: ("Cadastrar novo participante", cadastrar_participante),
        2: ("Realizar inscrição em eventos", inscricao_evento),
        3: ("Buscar participante por código", procurar_participante),
        4: ("Atualizar e-mail", atualizar_email),
        5: ("Remover participante", deletar_participante),
    }
    menu_geral(f'{"PARTICIPANTE":^40}', opcoes)

def inscricao_evento():
    from util import existencia
    from participante import participantes
    from evento import eventos
    exibir_eventos()
    #se nenhum evento tiver cadastrado ja para
    try:
        id_evento = int(input("Digite o ID do evento: "))
        id_participante = int(input("Digite o ID do participante: "))
    except ValueError:
        print("ID inválido.")
        return        
    evento = existencia(id_evento, eventos)
    participante = existencia(id_participante, participantes)
    if id_evento in participante['eventos']:
        print("O participante já está inscrito nesse evento!")
    else:
        participante['eventos'].append(id_evento)
        evento['participantes'].append(id_participante)
        print(f"{participante['nome']} inscrito no evento {evento['nome']} com sucesso!")
