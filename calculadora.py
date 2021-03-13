def soma(numero1, numero2):
    return numero1 + numero2


def subtracao(numero1, numero2):
    return numero1 - numero2


def multiplicacao(numero1, numero2):
    return numero1 * numero2


def divisao(numero1, numero2):
    return numero1 / numero2


def calculo(operacao, numero1, numero2):
    if operacao == '+':
        return soma(numero1, numero2)
    elif operacao == '-':
        return subtracao(numero1, numero2)
    elif operacao == '*':
        return multiplicacao(numero1, numero2)
    elif operacao == '/':
        return divisao(numero1, numero2)


def calculadora():
    print("CALCULADORA")
    numero1 = int(input('Digite o primeiro numero: '))
    numero2 = int(input('Digite o segundo numero: '))
    operacao = input('Digite a operação [+ - * /]: ')

    resultado = calculo(operacao, numero1, numero2)
    print('Resultado: '+str(resultado))

    input('...')


calculadora()
