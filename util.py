import os
from datetime import datetime

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
    return {id: p for id, p in participantes.items() if id in evento['participantes']}
#aqui dava pra usar filter mas tava retornando uma lista de tuplas, por isso mudei pra dicio, pra ficar melhor pra tratar

def ler_id(mensagem="Digite o ID: "):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("ID inválido.")

def existencia(id, dicionario):
    item = dicionario.get(id)
    if item:
        return item
    print("ID não encontrado.")
    return None

def tratar_data(mensagem= "Data do evento (dd/mm/aaaa): "):
    while True: 
        try:
            data_recebida = input(mensagem)
            data = datetime.strptime(data_recebida, "%d/%m/%Y").date()
            #arrumar a forma que mostra
            return data
        except ValueError:
                print("Data/hora inválida. Tente novamente.")