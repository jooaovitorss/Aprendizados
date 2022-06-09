from tkinter import N


print("*********************** Python Calculator **********************")
print("\nSelecione o número da opção desejada:")
print("\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")

op = int(input("Digite a sua opção (1/2/3/4): "))

if op != 1:
    print("Operação invalida")

primeiro_número = int(input("Digite o primeiro numero: "))

segundo_número = int(input("\nDigite o segundo numero: "))

if op == 1:
    soma = (primeiro_número + segundo_número)
    print(soma)
if op == 2:
    sub = (primeiro_número - segundo_número)
    print(sub)
if op == 3:
    multiply = (primeiro_número * segundo_número)
    print(multiply)
if op == 4:
    divisão = (primeiro_número / segundo_número)
    print(divisão)

