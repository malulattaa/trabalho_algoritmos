from dados import *
from temas import temas

def participantes_ativos():
    """ lista os participantes que estão inscritos em vários eventos"""
    ativos = sorted([(p['nome'], len(p['eventos'])) for p in participantes.values() if len(p['eventos']) >1], key = lambda item: item[1], reverse=True)
    
    print("Participantes mais ativos: ")
    if ativos:
        for nome, qtde in ativos:
            print(f"{nome} - {qtde} eventos inscritos.")
    else:
        print("Não há participante inscrito em mais de um evento.")
def temas_preferidos():
    """ mostra os temas preferidos dos participantes"""
    temas = set(tema for p in participantes.values() for tema in p['pref_tematica'])
    
    print("Temas preferidos dos participantes: ")
    for pref in temas:
        print(f" - {pref}")

def poucos_participantes():
    """mostra eventos com menos de 2 participantes para possível cancelamento"""
    qtde_participantes = [e['nome'] for e in eventos.values() if len(e['participantes']) < 2]
    if qtde_participantes:
        print("Eventos com menos de 2 participantes: ")
        for nome in qtde_participantes:
            print(f" - {nome}")
    else:
        print("Não há eventos com menos de 2 (dois) participantes.")
        
def media_participantes_por_tema():
    """ cálculo da média de participantes que um tema tem"""
    
    for tema in temas:
        evento_tema = [e for e in eventos.values() if e['tema'] == tema]
        if evento_tema:
            participantes_tema = sum(len(e['participantes']) for e in evento_tema)
            media = participantes_tema/ len(evento_tema)
        else:
            media = 0
        
        print(f"O tema {tema} tem a média de {media} participantes por tema")
        print("")