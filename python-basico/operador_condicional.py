# Operadores condicionais.
# Estrutura condicional é uma seção que ajuda a definir condições para a execução de determinados blocos de código, em
# vez de executar tudo de uma vez, sem nenhuma interrupção, o programa executa um teste e executa um determinado bloco
# de código a partir do resultado desse teste.

# se a condição do if for True, o bloco de código dentro do 'escopo' do if é executado.
if 5 > 3:
    print("5 > 3 =", 5 > 3)

# como a condição abaixo é falsa o bloco de código não será executado.
if 5 > 7:
    print("5 > 7 =", 5 > 7)
# o print teste está fora do 'escopo' do if então sempre será executado.
print("teste")

# além do if podemos ter o else, que será executado caso a condição do if seja falsa.
if 5 > 7:
    print("5 > 7 =", 5 > 7)
else:
    print("5 > 7 =", 5 > 7)

# quando temos que lidar com mais uma condição que especifique outra regra podemos usar o elif.
n = 3
if n == 5:
    print("n == 5 =", n == 5)
elif n == 4:
    print("n == 4 =", n == 4)
elif n == 3:
    print("n == 3 =", n == 3)
else:
    print(n)

# podemos unir operadores condicionais e lógicos para ter condicionais mais complexas.
x = 2
if(x > 1 and n <= 3):
    print(f"{x} e maior que 1 e {n} e menor ou igual a 3")
else:
    print("uma ou nenhuma das condicoes foram verdadeiras")