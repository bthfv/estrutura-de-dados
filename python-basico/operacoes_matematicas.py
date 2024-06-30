# Operações matemáticas.
a = 5
b = 3

print(a, b)

# para realizar soma usamos  o operador +.
print(f"soma de {a} + {b} = {a + b}")

# para realizar uma subtração usamos o operador -.
print(f"subtracao de {a} - {b} = {a - b}")

# para realizar uma divisão usamos o operador /.
print(f"divisao de {a} / {b} = {a / b}")

# para realizar uma multiplicação usamos o operador *.
print(f"divisao de {a} * {b} = {a * b}")

# temos o operador de resto da divisão que é o %.
print(f"resto da divisao de {a} por {b} = {a % b}")
print("resto da divisao de 10 por 5 =", 10 % 5)

# podemos realizar a potenciação por meio do operador **.
print(f"{a} elevado a {b} = {a ** b}")

# para importar módulos do python utilizamos o comando import.
import math

# função sqrt do módulo math recebe como parâmetro um valor e retorna a raiz quadrada dele.
print("raiz quadrada de 81 =", math.sqrt(81))

casos_doencas = 134
numero_habitantes = 34432
casos_por_habitantes = casos_doencas / numero_habitantes

# por meio da função round do python podemos delimitar a quantidade de casas decimais de um valor.
print("casos por habitantes:", round(casos_por_habitantes, 6))