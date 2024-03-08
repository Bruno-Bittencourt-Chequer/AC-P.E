#Verificar se é vogal ou consoante

def e_vogal(letra):
    match letra:
        case "a"|"e"|"i"|"o"|"u":
            return "e vogal"
    return "é consoante"

print(e_vogal("g"))
print(e_vogal("a"))
    
