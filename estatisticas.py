from dados import participantes

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
        
        