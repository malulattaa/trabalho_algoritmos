from collections import Counter
from util import ler_id, existencia, limpar_tela, ler_opcao


temas = ["Inteligência Artificial", "Web", "Segurança", "Rede", "Programação", "Banco de dados", "Mobile", "Computação em Nuvem", "Robótica"]
def menu_temas():
    """ 
    menu de temas disponíveis retornando o tema escolhido
    """
    #solução temporaria
    #limpar
    print("_" * 15, "TEMAS", "_" * 15)
    #por isso com meni geral
    print("1 - Inteligência Artificial - IA")
    print("2 - Web")
    print("3 - Segurança")
    print("4 - Redes")
    print("5 - Programação")
    print("6 - Banco de Dados")
    print("7 - Mobile")
    print("8 - Computação em Nuvem")
    print("9 - Robótica")
    print("0 - Voltar")
    op = ler_opcao(len(temas))
    # if op == 0:
    #     return None
    return temas[op - 1]

def trocar_tema():
    """ 
    troca de tema de um evento especifico
    """
    from evento import eventos, exibir_eventos
    from temas import menu_temas 
    #em caso de trocar o tema pelo tema que ja etsa, escrever algo
    limpar_tela()
    exibir_eventos()
    id_evento = ler_id("Digite o id do evento que deseja trocar o tema: ")
    #escrever se nao for o certo
    evento = existencia(id_evento, eventos)
    if evento:
        print(f"{evento['nome']}")
        print(f"{evento['tema']}")
        print(f"Deseja trocar o tema do evento {evento['nome']} por qual tema? ")
        tema_novo = menu_temas()
        evento['tema'] = tema_novo
        print(f"O tema do evento {evento['nome']} foi alterado para {tema_novo}.")

def agrupar_tema():
    """ 
    exibe a quantidade de eventos por tema
    """
    from evento import eventos
    agrupar = {
        tema: {id: evento for id, evento in eventos.items() if evento['tema'] == tema} for tema in temas
    }
    for tema, lista_evento in agrupar.items():
        print(f"{tema} - {len(lista_evento)} eventos")
        for id, evento in lista_evento.items():
            print(f" - {id} - {evento['nome']}")
            print("")
            #precisa de mais alguma coisa alem de id e nome?