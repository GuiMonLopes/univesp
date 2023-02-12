#Realizar a leitura dos valores de quatro notas escolares bimestrais de um aluno representadas pelas
# variáveis N1, N2, N3 e N4. Calcular a média aritmética (variável MD) desse aluno e apresentar a mensagem
# “Aluno Aprovado com média” se a média obtida for maior ou igual a 5; caso contrário,
# apresentar a mensagem “Aluno Reprovado com média”.
# Informar também, após a apresentação das mensagens, o valor da média obtida pelo aluno.


print("####################################")
print("Bem-vindo ao calculo de notas!")
print("####################################")

notas = []
media = 0

for interacao in range(1,5):
    notas.append(float(input("Digite a nota {}: ".format(interacao))))

print("As notas inseridas: {}".format(notas))

media = sum(notas)/len(notas)

print("A média das notas é: {:.2f}".format(media))

print("####################################")
print("Fim do Programa!")
print("####################################")