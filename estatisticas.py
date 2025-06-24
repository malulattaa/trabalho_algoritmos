from dados import *

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
    
    if not eventos:
        print("Não há evento cadastrado.")
        return
    
    for evento in eventos.values():
        tema = evento['tema']
        num_participantes = len(evento['participantes'])
        
        
        media_tema = {}
        if tema not in media_tema:
            media_tema[tema] = {
                'eventos' : 0,
                "participantes" : 0
            } 
        
        media_tema[tema]['eventos'] += 1
        media_tema[tema]['participantes'] += num_participantes
        
    print("Taxa média de participantes por tema: ")
    for tema, dados in media_tema.items():
        media = dados['participantes'] / dados['eventos']
        print(f"{tema} - {media} participantes por evento.")