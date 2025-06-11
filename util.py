import os
from participante import cadastrar_participante

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
def verificar_participantes(evento, participantes):
    return list(filter(lambda p: p['id'] in evento['participantes'], participantes))
    """ if not filtrar:
        print("Nenhum participante inscrito nesse evento.")
    return filtrar"""

def ler_id(mensagem="Digite o ID: "):
    from participante import participantes
    from evento import eventos
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("ID inválido.")

def existencia(id, lista):
    item = next((i for i in lista if i['id'] == id), None)
    if not item:
        print(f"ID não encontrado.")
    return item