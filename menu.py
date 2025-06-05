#from util import limpar_tela
from participante import cadastrar_participante
from evento import cadastrar_evento


def ler_opcao(lim_sup):
    #ler a opção ate que seja valido 
    while True:
        try:
            op = int(input("Escolha a opção: "))
            if op >= 0 and op <= lim_sup:
                return op
            else:
                print(f"Opção fora do intervalo. Digite um número entre 0 e {lim_sup}")
        except ValueError:
            print("Você não digitou uma opção válida")
        

def menu_principal():
    #limpar
    print("_" * 20, "MENU", "_" * 20)
    print("1 - Gerenciar participantes")
    print("2 - Gerenciar eventos")
    #troca de tema ou atualização de e-mail
    print("3 - Estastísticas e relatórios") 
    #participantes mais ativos e temas mais frequentes
    #ver se quer remover particpante ou evento
    print("0 - Sair")
    op = ler_opcao(3)
    
    opcoes = {
        1: menu_participantes,
        2: menu_eventos,
        #3:
        
    }
    
    if op == 0:
        print("Encerrando.")
        return    

    if op in opcoes:
        opcoes[op]()
    else:
        print("Opção inválida.")


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
    print("1 - Cadastrar novo evento") #ok
    print("2 - Exibir todos os eventos") #ok
    print("3 - Listar participantes do evento") #ok
    print("4 - Remover evento") #ok
    print("5 - Buscar eventos por tema") #ok
    #contabilizar quantos eventos cada tema possui
    #pode incluir aq a taxa media de participação por tema?
    print("6 - Agrupar por tema") 
    print("0 - Voltar ao menu anterior") 
    op = ler_opcao(6)
def menu_participantes():
    #limpar
    print(f'"_" * 20, {"PARTICIPANTE":^40}, "_" * 20')
    print("1 - Cadastrar novo participante")
    print("2 - Buscar participante por código") #ok
    print("3 - Listar eventos do participante") #ok
    print("4 - Atualizar e-mail ou tema") #ok
    #nao sei se é melhor fazer isso separado ou junto e abrir outro menu pra escolher
    print("5 - Remover participante") #ok
    print("6 - Verificar duplicatas")#ok
    print("7 - Buscar participante por data ou tema") #ok
    #isso tb vale pra participante? la n ta especificando
    print("0 - Voltar ao menu anterior")
    op = ler_opcao(7)
    
