cadastros = list()
usuario = dict()
p = 1
cont = 0

def idade():
    while True:
        try:
            idade = int(input('Idade: '))
            break
        except:
            print('ERRO! Idade deve ser digitada de forma numérica, tente novamente.')
    return idade

def sexo():
    while True:
        sexo = input('Sexo [M/F]: ').lower()
        if sexo in 'mf':
            break
        else:
            print('ERRO! Responda com "M" ou "F".')
    return sexo

def media_idade():
    soma = 0
    for a in cadastros:
        soma += a['idade']
    media = soma / cont
    return media

def nome_mulheres():
    nomes = ''
    cont2 = 0
    for a in cadastros:
        if a['sexo'] == 'f':
            nomes += f'{a['nome']}, '
    return nomes.strip(', ')

def acima_media():
    cont3 = 0
    for a in cadastros:
        for k, v in a.items():
            if k == 'idade' and v > media_idade():
                for z, w in cadastros[cont3].items():
                    print(f'{z} = {w},', end=' ')
                print('\n')
        cont3 += 1

########################################################################################################################

while p == 1:
    cont += 1
    usuario['nome'] = input('Nome: ')

    usuario['idade'] = idade()

    usuario['sexo'] = sexo()

    cadastros.append(usuario.copy())
    usuario.clear()

    while True:
        try:
            p = int(input('Deseja continuar? [ 0 -> Não ] [ 1 -> Sim]: '))
            break
        except:
            print('ERRO! Responda com "S" ou "N".')


print('==' * 20)
print(f'Ao todo, temos {cont} pessoas cadastradas.')
print(f'A média de idade dos usuários é de {media_idade():.0f}')
print(f'As mulheres cadastradas são: {nome_mulheres()}')
print(f'Os usuários acima da média de idade são:')
acima_media()
print('==' * 20)
print('Até breve!')
