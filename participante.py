participantes = []

def cadastrar_participante():
    #o id deve ser gerado automatico?
    nome = input("Nome completo: ")
    email = input("e-mail: ")
    pref_tematica = input("Preferência temática: ") #?


    participante = {
        'nome' : nome,
        'email' : email, #ver se pode por e-mal
        'pref_tematica' : pref_tematica,
    }
    participantes.append(participante)
