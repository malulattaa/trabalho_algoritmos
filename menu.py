from util import ler_opcao, limpar_tela, menu_geral, ler_id, existencia
from participante import cadastrar_participante, procurar_participante, atualizar_email, deletar_participante, inscricao_evento
from estatisticas import estatisticas
from evento import cadastrar_evento, exibir_eventos, listar_participantes_evento, deletar_evento, filtrar_evento
from temas import trocar_tema, menu_temas, agrupar_tema

def menu_principal():
    limpar_tela()
    opcoes = {
        1: ("Gerenciar participantes", menu_participantes),
        2: ("Gerenciar eventos", menu_eventos),
        3: ("Estatísticas e relatórios", estatisticas),
    }
    menu_geral(f'{"MENU":^40}', opcoes)

def menu_eventos():
    limpar_tela()
    opcoes = {
        1: ("Cadastrar novo evento", cadastrar_evento),
        2: ("Exibir lista de eventos", exibir_eventos),
        3: ("Listar participantes por evento", listar_participantes_evento),
        4: ("Remover evento", deletar_evento),
        5: ("Trocar tema de um evento", trocar_tema),
        6: ("Filtrar evento por tema/data", filtrar_evento),
        7: ("Agrupar por tema", agrupar_tema),
        #contabilizar quantos eventos tem aquel tema
    }
    menu_geral(f'{"EVENTO":^40}', opcoes)
    
def menu_participantes():
    limpar_tela()
    opcoes = {
        1: ("Cadastrar novo participante", cadastrar_participante),
        2: ("Realizar inscrição em eventos", inscricao_evento),
        3: ("Buscar participante por código", procurar_participante),
        4: ("Atualizar e-mail", atualizar_email),
        5: ("Remover participante", deletar_participante),
    }
    menu_geral(f'{"PARTICIPANTE":^40}', opcoes)


