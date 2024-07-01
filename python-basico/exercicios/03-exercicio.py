# leia a idade do usuário e classifique-o em:
# - criança - 0 a 12 anos.
# - adolescente - 13 a 17 anos.
# - adulto - acima de 18 anos.
# - caso seja digitado um número negativo mostrar uma mensagem de idade inválida.

idade = int(input("digite sua idade: "))

if idade >= 0 and idade <= 12:
    print("crianca")
elif idade >= 13 and idade <= 17:
    print("adolescente")
elif idade >= 18:
    print("adulto")
else:
    print("idade invalida")