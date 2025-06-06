from util import limpar_tela, ler_opcao
from participante import cadastrar_participante
from evento import cadastrar_evento
from estatisticas import estatisticas

def menu_principal():
    #limpar
    print("_" * 20, "MENU", "_" * 20)
    print("1 - Gerenciar participantes")
    print("2 - Gerenciar eventos")
    print("3 - Estastísticas e relatórios") 
    print("0 - Sair")
    op = ler_opcao(3)
    
    opcoes = {
        1: menu_participantes,
        2: menu_eventos,
        3: estatisticas,
        
        
    }
    if op == 0:
        print("Encerrando.")
        return    
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
    print("_" * 20, "EVENTO", "_" * 20)
    print("1 - Cadastrar novo evento") 
    print("2 - Exibir lista de eventos") 
    print("3 - Listar participantes por evento") 
    print("4 - Remover evento") 
    print("5 - Trocar tema de um evento")
    print("5 - Filtrar evento por tema/data") 
    print("6 - Agrupar por tema") 
    print("0 - Voltar ao menu anterior") 
    op = ler_opcao(6)
def menu_participantes():
    #limpar
    print(f'{"PARTICIPANTE":^40}')
    print("")
    print("1 - Cadastrar novo participante")
    print("2 - Buscar participante por código") 
    print("3 - Atualizar e-mail") 
    #nao sei se é melhor fazer isso separado ou junto e abrir outro menu pra escolher
    print("4 - Remover participante") 
    #isso tb vale pra participante? la n ta especificando
    print("0 - Voltar ao menu anterior")
    op = ler_opcao(4)
    
