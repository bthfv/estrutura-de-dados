# Operadores lógicos e relacionais.
a = True 
b = False 

print(a, b)

# operador and corresponde a uma conjunção lógica, também podemos usar '&' no lugar do 'and'.
print("conjuncao logica: ")
print("True and True =", True and True)
print(f"{a} and {b} = {a and b}")
print(f"{b} and {a} = {b and a}")
print("False and False =", False and False)

# operador or corresponde a uma disjunção lógica, também podemos usar '|' no lugar do 'or'.
print("disjuncao logica: ")
print("True or True =", True or True)
print(f"{a} or {b} = {a or b}")
print(f"{b} or {a} = {b or a}")
print("False or False =", False or False)

# operador not corresponde a negação lógica, também podemos usar '!' no lugar do 'not'.
print("negacao logica: ")
print(f"not {a} = {not a}")
print(f"not {b} = {not b}")

# operações relacionais são operações que comparam valores e nos retornam um valor booleano.
# caso a comparação seja verdadeira temos como retorno True, caso não temos como retorno False.
print("operacoes relacionais: ")
print("5 > 3 =", 5 > 3) # operador '>' checa se o valor da esquerda é maior que o da direita.
print("5 >= 3 =", 5 >= 3) # operador '>=' checa se o valor da esquerda é maior ou igual ao da direita.
print("5 < 3 =", 5 < 3) # operador '<' checa se o valor da esquerda é menor que o da direita.
print("5 <= 3 =", 5 <= 3) # operador '<=' checa se o valor da esquerda é menor ou igual ao da direita.
print("5 == 3 =", 5 == 3) # operador '==' checa se os valores são iguais.
print("5 != 3 =", 5 != 3) # operador '!=' checa se os valores são diferentes.
