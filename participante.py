from temas import menu_temas
from evento import exibir_eventos
participantes = []

id_participante = 1
def cadastrar_participante():
    global id_participante
    nome = input("Nome completo: ")
    email = input("e-mail: ")
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
        'id': id_participante,
        'nome' : nome,
        'email' : email, #ver se pode por e-mal
        'pref_tematica' : preferencia,
        'eventos' : []
    }
    participantes.append(participante)
    id_participante += 1
    print(f"Participante {nome} cadastrado com sucesso!")
    

    

