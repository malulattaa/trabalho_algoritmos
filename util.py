import os

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


def limpar_tela():
    os.system("cls" if os.name == 'nt' else 'clear')
    
def menu_geral(titulo, opcoes):
    while True:
        #limpar_tela()
        print(f'{titulo.upper():^40}')
        for num_opcao, (descricao, _) in opcoes.items():
            print(f"{num_opcao}: {descricao}")
        print("0 - Voltar")
        op = ler_opcao(max(opcoes.keys()))
        if op == 0:
            break
        _, funcao = opcoes[op]
        funcao()
        
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