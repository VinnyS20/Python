palavra_secreta = 'bongu'
letras_acertadas = ''

while True:
    letra_digitada = input('Digite uma letra: ')

    if len(letra_digitada) > 1:
        print('Uma letra por vez, colega.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada =''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas: 
            palavra_formada += letra_secreta
        else:
           palavra_formada +='*'
    print(palavra_formada)
    


