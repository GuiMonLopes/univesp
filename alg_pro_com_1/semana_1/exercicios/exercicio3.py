#Desenvolver os diagramas de blocos e as codificações em português estruturado usando
# laço incondicional (para) do seguinte problema:
# Construir um programa que apresente a soma dos cem primeiros números naturais
# (1 + 2 + 3 +...+ 98 + 99 + 100).

print("####################################")
print("Soma de números naturais!")
print("####################################")

soma_dos_numeros_naturais = 0

for numeros_naturais in range(1,101):
    soma_dos_numeros_naturais += numeros_naturais
    print(numeros_naturais)

print("Soma dos numeros naturais de 1 a 100: {}".format(soma_dos_numeros_naturais))

