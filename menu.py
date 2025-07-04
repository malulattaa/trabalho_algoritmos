from util import limpar_tela, menu_geral, ler_id, existencia
from participante import cadastrar_participante, procurar_participante, atualizar_email, deletar_participante, inscricao_evento, listar_participantes
from estatisticas import *
from evento import cadastrar_evento, alterar_evento, exibir_eventos, listar_participantes_evento, deletar_evento, filtrar_evento
from temas import agrupar_tema

def menu_principal():
    limpar_tela()
    opcoes = {
        1: ("Gerenciar participantes", menu_participantes),
        2: ("Gerenciar eventos", menu_eventos),
        3: ("Estatísticas e relatórios", menu_estatisticas),
    }
    menu_geral("MENU", opcoes)

def menu_eventos():
    limpar_tela()
    opcoes = {
        1: ("Cadastrar novo evento", cadastrar_evento),
        2: ("Exibir lista de eventos", exibir_eventos),
        3: ("Listar participantes por evento", listar_participantes_evento),
        4: ("Remover evento", deletar_evento),
        5: ("Editar dados do evento", alterar_evento),
        6: ("Filtrar evento por tema/data", filtrar_evento),
        7: ("Agrupar por tema", agrupar_tema),
    }
    menu_geral("EVENTO", opcoes)
    
def menu_participantes():
    limpar_tela()
    opcoes = {
        1: ("Cadastrar novo participante", cadastrar_participante),
        2: ("Lista de participantes", listar_participantes),
        3: ("Realizar inscrição em eventos", inscricao_evento),
        4: ("Buscar participante por código", procurar_participante),
        5: ("Atualizar e-mail", atualizar_email),
        6: ("Remover participante", deletar_participante),
    }
    menu_geral("PARTICIPANTE", opcoes)

def menu_estatisticas():
    limpar_tela()
    opcoes = {
        1: ("Participantes mais ativos", participantes_ativos),
        2: ("Taxa média de participação por tema", media_participantes_por_tema),
        3: ("Eventos com poucos participantes", poucos_participantes),
        4: ("Temas frequentes", temas_frequentes),
        5: ("Resumo geral do sistema", resumo_geral),
        6: ("Eventos mais populares", eventos_populares),
        
    }
    menu_geral("ESTATÍSTICAS E RELATÓRIOS", opcoes)
