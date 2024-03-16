#EX02: DIAS DA SEMANA

def dia_semana(dias):
    match dias:
        case 1:
            return "DOMINGO"
        case 2:
            return "SEGUNDA-FEIRA"
        case 3:
            return "TERÇA-FEIRA"
        case 4:
            return "QUARTA-FEIRA"
        case 5:
            return "QUINTA-FEIRA"
        case 6:
            return "SEXTA-FEIRA"
        case 7:
            return "SÁBADO"
        case _:
            return ""

