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
    op = ler_opcao(len(temas))
    return temas[op - 1]

def trocar_tema():
    from util import buscar_evento, verificar_id
    from evento import eventos
    tema_evento = verificar_id("Digite o id do evento que deseja trocar o tema: ")
    #escrever se nao for o certo
    evento = buscar_evento(tema_evento, eventos)
    if evento:
        print(f"{evento['nome']}")
        print(f"{evento['tema']}")
        print(f"Deseja trocar o tema do evento {evento['nome']} por qual tema? ")
        tema_novo = menu_temas()
        evento['tema'] = tema_novo
        print(f"O tema do evento {evento['nome']} foi alterado para {tema_novo}.")
    