Aluno = 'João Vitor'
nota1 = 7.5
nota2 = 4.8

# Definimos o que é "verificar uma aprovação"
def verificar_aprovacao():
    media = calcular_media([nota1, nota2])

    if media >= 6:
        print(f'o aluno {Aluno} foi aprovado')
    else:
        print(f'o aluno {Aluno} foi reprovado')

#definindo o que é calcular a média
def calcular_media(notas):
    quantidade = len(notas)

    soma = 0
    for nota in notas:
        soma = soma + nota

    media = soma / quantidade

    return media

# Chamando (executando) a função de verificar aprovação
verificar_aprovacao()
