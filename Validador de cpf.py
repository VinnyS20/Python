cpf_enviado = '52216910007'
nove_digitos = cpf_enviado [:9]
contador_regressivo_1 =10

resultado_digito1 = 0
for digito in nove_digitos:
    resultado_digito1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1 

digito_1 =(resultado_digito1 *10 ) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito2 = 0
for digito in dez_digitos :
    resultado_digito2 += int(digito)* contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito2 *10 ) %11
digito_2 = digito_2 if digito_2 <=9 else 0

novo_cpf = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado == novo_cpf :
    print(f'{cpf_enviado}O cpf é valido')
else:
    print('cpf invalido')