from dados import *
from temas import temas
from util import limpar_tela, titulos, sair_tela
from collections import Counter

def participantes_ativos():
    """ lista os participantes que estão inscritos em vários eventos"""
    limpar_tela()
    titulos("PARTICIPANTES MAIS ATIVOS")
    ativos = sorted([(p['nome'], len(p['eventos'])) for p in participantes.values() if len(p['eventos']) >1], key = lambda item: item[1], reverse=True)
    # mostra os participantes que estão inscritos em mais de um evento, ordenados pela quantidade de eventos inscritos
    if ativos:
        for nome, qtde in ativos:
            print(f"{nome}: {qtde} eventos inscritos.")
    else:
        print("Não há participante inscrito em mais de um evento.")
        print("")
    sair_tela()
        
def media_participantes_por_tema():
    """ cálculo da média de participantes que um tema tem"""
    limpar_tela()
    titulos("MÉDIA DE PARTICIPANTES POR TEMA")
    for tema in temas:
        evento_tema = [e for e in eventos.values() if e['tema'] == tema]
        if evento_tema:
            participantes_tema = sum(len(e['participantes']) for e in evento_tema)
            media = round(participantes_tema / len(evento_tema), 2)
            # calcula e arredonda a média de participantes por tema
        else:
            media = 0
        
        print(f"{tema:<30} | Média: {media} participante(s) por evento")
        #alinha o nome do tema à esquerda com até 30 caracteres
        print("")
    sair_tela()
def poucos_participantes():
    """mostra eventos com menos de 2 participantes para possível cancelamento"""
    limpar_tela()
    titulos("EVENTOS COM MENOS DE 2 PARTICIPANTES")
    qtde_participantes = [e['nome'] for e in eventos.values() if len(e['participantes']) < 2]
    if qtde_participantes:
        for nome in qtde_participantes:
            print(f" - {nome}")
    else:
        print("Todos os eventos tem pelo menos 2 participantes.")
    sair_tela()
def temas_frequentes():
    """ mostra os temas mais frequentes em eventos"""
    limpar_tela()
    titulos("TEMAS FREQUENTES")
    if not eventos:
        print("Nenhum evento cadastrado.")
        return
    temas = [evento['tema'] for evento in eventos.values()]
    
    contagem = Counter(temas)
    for tema, quantidade in contagem.items():
        print(f" - {tema}: {quantidade} evento(s)")
    
    print("")
    sair_tela()
        
def resumo_geral():
    """ exibe um resumo geral do sistema com total de participantes, eventos e temas """
    limpar_tela()
    titulos("RESUMO GERAL DO SISTEMA")
    print(f"Total de participantes: {len(participantes)}")
    print(f"Total de eventos: {len(eventos)}")
    print(f"Temas disponíveis: {len(temas)}")
    sair_tela()
    
def eventos_populares():
    """ lista os 5 eventos mais populares com base no número de participantes """
    limpar_tela()
    titulos("TOP 5 EVENTOS MAIS POPULARES")
    
    if not eventos:
        print("Nenhum evento cadastrado.")
        return
    
    populares = sorted(eventos.items(), key = lambda pop: len(pop[1]['participantes']), reverse=True)
    # ordena os eventos pela quantidade de participantes em ordem decrescente
    
    for id, evento in populares[:5]:
        print(f"{evento['nome']} | {len(evento['participantes'])} participantes")
    sair_tela()

