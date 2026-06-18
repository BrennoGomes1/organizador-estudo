from datetime import date

def calcular_urgencia(atividade):
    hoje = date.today()
    data_limite = atividade[3]
    peso = atividade[4]
    confianca = atividade[5]
    
    dias_restantes = (data_limite - hoje).days
    
    if dias_restantes <= 0:
        return 999  
    
    urgencia = (peso * (10 - confianca)) / dias_restantes
    return urgencia