def numero_quadrado(numero):
    quadrado = numero * numero      #ou ==> numero **2

    return quadrado
def calcular_imc(peso, altura):
    altura_quadrada = numero_quadrado(altura)

    imc = peso / altura_quadrada

    return  imc

def classificar(imc):
    if imc < 18.5:
        print('Magreza')
    elif imc >= 18.5 and imc < 25:
        print('Normal')
    elif imc >= 25 and imc < 30:
        print('Sobrepeso')
    elif imc >=30 and imc < 40:
        print('Obesidade')
    elif imc > 40:
        print('Obesidade Grave')

peso = float(input('insira seu peso(kg): '))
altura = float(input('insira sua altura(m): '))

meu_imc = calcular_imc(peso, altura)

classificar(meu_imc)
