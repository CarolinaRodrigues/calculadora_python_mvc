def soma(numero1, numero2):
	print(numero1 + numero2)
def subtracao(numero1, numero2):
	print(numero1 - numero2)

def multiplicacao(numero1, numero2):
	print(numero1 * numero2)

def divisao(numero1, numero2):
	print(numero1 / numero2)

def calculo(operacao, numero1, numero2):
	if operacao == '+':
		soma(numero1, numero2)
	elif operacao == '-':
		subtracao(numero1,numero2)
	elif operacao == '*':
		multiplicacao(numero1,numero2)
	elif operacao == '/':
		divisao(numero1,numero2)
	else:
		print('Operacao invalido')

def calculadora():
	numero1 = int(input('Digite o primeiro numero: '))
	numero2 = int(input('Digite o segundo numero: '))
	operacao = input ('Digite a operação [+ - * /]: ')

	calculo(operacao,numero1,numero2)
        
	input ('...')

calculadora()
