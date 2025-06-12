from collections import Counter
def menu_temas():
    from util import ler_opcao 
    #solução temporaria
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
    print("0 - Voltar")
    op = ler_opcao(len(temas))
    return temas[op - 1]

def trocar_tema():
    from util import existencia, ler_id, limpar_tela
    from evento import eventos, exibir_eventos
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
    
#7: ("Agrupar por tema", cadastrar_evento)

def agrupar_tema():
    from temas import temas
    from evento import eventos
    #ideia: mostrar todos os temas e a quantidade de eventos respectiva a aquele tema
    #em seguida: mostrar os eventos (nome e id?)
    #iteravel começa valendo 0
    #vai percorrendo um for pra passar por todos os elementos de temas
    #percorre a lista de eventos e ve quantos os i sao iguais
    agrupar = {
        tema: list(filter(lambda x: x['tema'] == tema, eventos)) for tema in temas
    }
    for tema, lista_evento in agrupar.items():
        print(f"{tema} - {len(lista_evento)} eventos")
        for evento in lista_evento:
            print(f"{evento['id']} - {evento['nome']}")
            #precisa de mais alguma coisa alem de id e nome?