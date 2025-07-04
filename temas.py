from util import limpar_tela, ler_opcao, titulos, sair_tela
from dados import eventos

temas = ["Inteligência Artificial", "Web", "Segurança", "Rede", "Programação", "Banco de dados", "Mobile", "Computação em Nuvem", "Robótica"]
def menu_temas():
    """ 
    menu de temas disponíveis retornando o tema escolhido
    """
    limpar_tela()
    print("")
    print("PREFERÊNCIA TEMÁTICA".center(60, "-"))
    print("")
    print("1 - Inteligência Artificial - IA")
    print("2 - Web")
    print("3 - Segurança")
    print("4 - Redes")
    print("5 - Programação")
    print("6 - Banco de Dados")
    print("7 - Mobile")
    print("8 - Computação em Nuvem")
    print("9 - Robótica")
    while True:
        op = ler_opcao(len(temas))
        if op == 0:
            print("Opção fora do intervalo. Digite um número entre 1 e 9")
        else:
            return temas[op - 1]

def agrupar_tema():
    """ 
    exibe a quantidade de eventos por tema
    """
    limpar_tela()
    titulos("EVENTOS AGRUPADOS POR TEMA")
    agrupar = {
        tema: {id: evento for id, evento in eventos.items() if evento['tema'] == tema} for tema in temas
    }
    for tema, lista_evento in agrupar.items():
        print(f">> {tema} - {len(lista_evento)} eventos")
        for id, evento in lista_evento.items():
            print(f"   - Código do evento: {id} | {evento['nome']}")
        print("-"*60)
    sair_tela()