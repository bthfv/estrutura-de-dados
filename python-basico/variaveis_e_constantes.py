# Manipulação de variáveis e constantes.
# - por meio de variáveis que um algoritmo "guarda" os dados do problema
# - todo dado que tem a possibilidade de ser alterado no decorrer do tempo, deverá ser tratado como uma variável
# - quando um dado não tem nenhuma possibilidade de variar no decorrer do tempo, deverá ser tratado como constante

# Tipo de variáveis.
# - inteiros: valores positivos ou negativos, que não possuem uma parte fracionária. exemplos: 1, 30, 40, 12, -50
# - float ("real"): valores positivos ou negativos, que podem possuir uma parte fracionária (também podem ser inteiros).
# exemplos de float: 1.4, 6.7, 10.3, 100.0, -47.0
# - caracteres (string): qualquer elemento presente no teclado. exemplos: "maria", "joão", 'm', 'f'
# - lógico (booleano): verdadeiro ou falso. exemplos: true, false, 0, 1

# em python não especificamos o tipo de dados para a variável. python possui tipagem dinâmica.
numero = -3
numero_jogos = 14
numero_convidados = 15

# função print serve para exibir dados no console/terminal. 
# função type nos retorna o tipo do valor passado como parâmetro. 
print(type(numero), " valor: ", numero)
print(type(numero_jogos), " valor: ", numero_jogos)
print(type(numero_convidados), " valor: ", numero_convidados)

pi = 3.14159
numero_euler = 2.71828
escala_terremoto = -4.55

print(type(pi), " valor: ", pi)
print(type(numero_euler), " valor: ", numero_euler)
print(type(escala_terremoto), " valor: ", escala_terremoto)

# strings podem ser delimitadas tanto por aspas simples quanto duplas.
letra = 'w' 
palavra1 = "linguagem de programacao" 
palavra2 = "python"

print(type(letra), " valor: ", letra)
# usando virgula estamos fazendo concatenações de variáveis e strings.
print(type(palavra1), type(palavra2), " valor: ", palavra1, palavra2)

# podemos receber dados do usuário por meio da função input e armazenar o retorno em uma variável.
idade = input("digite sua idade: ")
# porém quando recebemos um dado do teclado pela função input esse dado é armazenado como uma string.
print("tipo de ", idade, " : ", type(idade))
print("sua idade e:", idade)

# podemos fazer a conversão dos valores recebidos pela função input pro tipo desejado.
# função float converte um dado para float.
ph = float(input("digite o ph do solo: "))
print("tipo de ", ph, " : ", type(ph))
print("o ph do solo foi igual a: ", ph)

# em python qualquer variável escrita em maiúscula é considerada uma constante
NOME = "bthfv"
print(NOME)