from util import menu_temas
participantes = []


def cadastrar_participante():
    #o id deve ser gerado automatico?
    nome = input("Nome completo: ")
    email = input("e-mail: ")
#fazer um while pra ver se quer continuar adicionando
#guardar todas as escolhidas em uma lista
    preferencia = []
    while True:
        sair = input("Deseja adicionar uma preferência temática? (S para sim)/(N para não): ").upper().strip()
        if sair == 'N':
            break
        elif sair == 'S':
            print(f'{"PREFERÊNCIA TEMÁTICA":^40}')
            tema = menu_temas() 
            preferencia.append(tema)
        else:
            print("Digite uma opção válida (S ou N).")

    participante = {
        #'id': id,
        'nome' : nome,
        'email' : email, #ver se pode por e-mal
        'pref_tematica' : preferencia,
    }
    participantes.append(participante)
    print(f"Participante {nome} cadastrado com sucesso!")

