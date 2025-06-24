import os
from datetime import datetime

def ler_opcao(lim_sup):
    """ 
    le a opcao do usuario, para que seja um numero dentro do intervalo valid
    """
    #le a opcao do usuario e só aceita um numero int dentro do intervalo estipulado como valido
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
    """ 
    limpa a tela do terminal
    """
    os.system("cls" if os.name == 'nt' else 'clear')
    #os.system() - Permite executar comandos do sistema operacional a partir do Python.
    #os.name - Retorna o nome do sistema operacional, nesse caso, windows é nt
    #Executa o comando cls (limpar tela no Windows)
    
def menu_geral(titulo, opcoes):
    """ 
    exibe um menu baseado em um dicionario de opções
    """
    while True:
        #limpar_tela()
        print(f'{titulo.upper():_^50}')
        for num_opcao, (descricao, _) in opcoes.items():
            print(f"{num_opcao}: {descricao}")
        print("0 - Voltar")
        op = ler_opcao(max(opcoes.keys()))
        #ler a opcao e o limite superior que ela recebe é o maior numero que existe nas chaves de opções
        if op == 0:
            break
        _, funcao = opcoes[op]
        funcao()
def verificar_participantes(evento, participantes):
    """ dicio com os participantes cadastrados em um evento"""
    return dict(filter(lambda item: item[0] in evento['participantes'], participantes.items()))
#aqui dava pra usar filter mas tava retornando uma lista de tuplas, por isso mudei pra dicio, pra ficar melhor pra tratar

def ler_id(mensagem="Digite o ID: "):
    """ 
    solicita um id ao usuário e retorna se for valido
    """
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("ID inválido.")

def existencia(id, dicionario):
    """ 
    verifica se o id informado existe no dicionario, se sim retorna o item correspondente
    """
    item = dicionario.get(id)
    if item:
        return item
    print("ID não encontrado.")
    return None

def tratar_data(mensagem= "Data do evento (dd/mm/aaaa): "):
    """ 
    solicita uma data ao usuário e valida
    """
    while True: 
        try:
            data_recebida = input(mensagem)
            data = datetime.strptime(data_recebida, "%d/%m/%Y").date()
            #arrumar a forma que mostra
            return data
        except ValueError:
                print("Data inválida. Tente novamente.")
                
def verificar_email(email, dicionario):
    """ 
    verifica se o email ja esta sendo usado
    """
    
    emails_existentes = set(p['email'] for p in dicionario.values())
    
    if email in emails_existentes:
        print("Esse e-mail já está sendo usado.")
        return