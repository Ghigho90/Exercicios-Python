# Solicita ao usuário o valor da temperatura em graus Celsius
c = float(input("Digite a temperatura em graus Celsius: "))

# Converte para Fahrenheit
f = (c * 9/5) + 32

# Converte para Kelvin
k = c + 273.15

# Exibe os resultados na tela
print("Temperatura em Fahrenheit:", f)
print("Temperatura em Kelvin:", k)