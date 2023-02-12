#Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit.
#A fórmula de conversão é F = C * 9 / 5 + 32, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

print("####################################")
print("Bem-vindo a conversão de temperatura!!")
print("####################################")
celsius_to_fahrenheit = False
fahrenheit_to_celsius = False
escolhe_da_conversao = 0
temperatura = 0
resultado = 0

print("Informe o tipo de conversão que gostaria de utilizar:"
      "\n(1) Celsius para Fahrenheit"
      "\n(2)Fahrenheit para Celsius ")

while True:
    escolhe_da_conversao = int(input("Digite a escolha: "))
    if escolhe_da_conversao == 1:
        celsius_to_fahrenheit = True
        break
    elif escolhe_da_conversao == 2:
        fahrenheit_to_celsius = True
        break
    else:
        print("Digite o tipo de conversão existente."
              "\n(1) Celsius para Fahrenheit"
              "\n(2)Fahrenheit para Celsius")
        continue

temperatura = float(input("Digite a temperatura para conversão: "))

if celsius_to_fahrenheit:
    resultado = (temperatura * (9/5)) + 32
    simbolo = "°F"

if fahrenheit_to_celsius:
    resultado = (temperatura - 32) * (5/9)
    simbolo = "°C"

print("A temperatura convertida é de {:.02f} {}".format(resultado, simbolo))

print("####################################")
print("Fim do programa!")
print("####################################")





