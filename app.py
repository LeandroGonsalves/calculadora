print("**********Calculadora Python**********")

print("Selecione a opção desejada \n")

print('1 - soma')
print('2 - subtração')
print('3 - multiplicação')
print('4 - divisão')

def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y

escolha = input("\nDigite sua opção: 1 / 2 / 3 / 4: \n")

num1 = int(input('Digite o primeiro numero da operação\n'))
num2 = int(input('\nDigite o segundo numero da operação\n'))

if escolha == '1':
    print(num1, "+", num2, "=", adicao(num1, num2))

elif escolha == '2':
    print(num1, "-", num2, "=", subtracao(num1, num2))

elif escolha == '3':
    print(num1, "*", num2, "=", multiplicacao(num1, num2))

elif escolha == '4':
    print(num1, "/", num2, "=", divisao(num1, num2))

else:
    print("opção inválida")