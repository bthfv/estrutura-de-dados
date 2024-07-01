# calcular a média de um aluno que cursou a disciplina de programação 1, a partir da leitura das notas m1, m2 e m3.
# passando por um cálculo de média aritmética. após a média calculada, devemos anunciar se o aluno foi aprovado, 
# reprovado ou pegame exame.
# se a média estiver entre 0.0 e 4.0, o aluno está reprovado.
# se a média estiver entre 4.1 e 6.0, o aluno pegou exame.
# se a média for maior do que 6.0, o aluno está aprovado.
# se o aluno pegou exame, deve ser lida a nota do exame, se a nota do exame for maior que 6.0, está aprovado, se não 
# está reprovado.

n1 = float(input("digite a nota m1: "))
n2 = float(input("digite a nota m2: "))
n3 = float(input("digite a nota m3: "))

media = (n1 + n2 + n3) / 3.0

if media >= 0.0 and media <= 4.0:
    print("reprovado")
elif media >= 4.1 and media <= 6.0:
    print("pegou exame")
    exame = float(input("digite a nota do exame: "))
    if exame > 6.0:
        print("aprovado")
    else:
        print("reprovado")
elif media > 6.0:
    print("aprovado")