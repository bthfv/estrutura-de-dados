# Manipulação de strings.
a = "casaco"
print(a)

# função upper() nos retorna o conteúdo da variável em maiúsculo.
maiuscula = a.upper()
print(maiuscula)

# função lower() nos retorna o conteúdo da variável em minúsculo.
minuscula = maiuscula.lower()
print(minuscula)

# função capitalize() nos retorna o conteúdo da variável apenas com a primeira letra em maiúsculo.
primeira_letra_maiuscula = minuscula.capitalize()
print(primeira_letra_maiuscula)

# podemos pegar apenas um determinado trecho de uma string e armazenalo em uma variável.
# uma string possui índices onde cada letra fica em um índice, os índices começam a partir do 0 que é a primeira letra.
# no formato abaixo quando pedimos a[0:3] o python não nos retornará o índice 3, mas sim até o anterior a ele.
metade_palavra = a[0:3]
print(metade_palavra)

# quando não passamos o segundo índice temos que o python percorre até o final da string.
ultimas_letras = a[3:]
print(ultimas_letras)

# também podemos trocar caracteres por outro por meio da função replace(), onde o primeiro parâmetro é o que vai ser 
# trocado e o segundo é pelo o que será trocado. (a string original continua inalterada, apenas temos o retorno com
# a substituição de uma nova string)
b = a.replace("aco", "inha")
print(b)

# detalhe que ocorre é a substituição de todas as ocorrências do padrão passado como parâmetro. (todos os 'o' viram 'a')
c = a.replace('o', 'a');
print(c)

# função find() recebe como parâmetro uma string e retorna o índice da primeira ocorrência dessa string.
# caso a string não seja encontrada temos como retorno -1.
print(c.find('a')) 

# função len() nos retorna o tamanho de uma string. espaços em branco também contam como caracteres dentro da string.
e = " casaco "
print(e)
print(len(e))

# função strip() remove os espaços em brancos no ínicio e fim de uma string e retorna uma nova string.
f = e.strip()
print(f)
print(len(f)) 

# f-strings serve para colocar variáveis dentro de um texto, e isso é feito utilizando a letra “f” antes do texto e 
# colocando a variável dentro de {}, também podemos realizar operações dentro do {}.
n1 = 14
n2 = 16
print(f"dividindo {n1} / {n2} = {n1 / n2}")