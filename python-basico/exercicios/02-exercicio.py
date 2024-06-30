# Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km 
# por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. 
# O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a 
# quantidade de litros utilizada na viagem

tempo_gasto = float(input("digite quantos minutos você gastou na viagem: "))
velocidade_media = float(input("digite a velocidade media em km/h: "))

distancia = (tempo_gasto / 60) * velocidade_media
litros_gastos = distancia / 12

print("velocidade media: ", velocidade_media)
print("tempo gasto em horas na viagem: ", tempo_gasto / 60)
print("distancia percorrida em km: ", distancia)
print("litros gastos: ", litros_gastos)