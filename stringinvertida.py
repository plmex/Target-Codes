string = str(input('Escreva o que quiser: '))
stringInvertida = ""

for letra in range(len(string) -1, -1, -1):
    stringInvertida += string[letra]
    
print(stringInvertida)
