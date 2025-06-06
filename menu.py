from util import ler_opcao, limpar_tela, menu_geral
from participante import cadastrar_participante
from estatisticas import estatisticas
from evento import cadastrar_evento, exibir_eventos


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
        #3: ("Listar participantes por evento", cadastrar_evento),
        #4: ("Remover evento", cadastrar_evento),
        #5: ("Trocar tema de um evento", cadastrar_evento),
        #6: ("Filtrar evento por tema/data", cadastrar_evento),
        #7: ("Agrupar por tema", cadastrar_evento),
    }
    menu_geral(f'{"EVENTO":^40}', opcoes)
def menu_participantes():
    opcoes = {
        1: ("Cadastrar novo participante", menu_participantes),
        2: ("Buscar participante por código", menu_eventos),
        3: ("Atualizar e-mail", estatisticas),
        4: ("Remover participante", estatisticas),
    }
    menu_geral(f'{"PARTICIPANTE":^40}', opcoes)
    
