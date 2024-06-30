# Ler dois números inteiros, executar e mostrar o resultado das seguintes operações: adição, subtração, 
# multiplicação e divisão.

n1 = int(input("digite um valor: "))
n2 = int(input("digite outro valor: "))

print("adicao: ", n1 + n2)
print("subtracao: ", n1 - n2)
print("multiplicacao: ", n1 * n2)

# caso o usuário digite um valor 0 para n2
try:
    print("divisao: ", float(n1) / n2)
except ZeroDivisionError:
    print("erro: divisao por zero")