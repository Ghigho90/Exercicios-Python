# Solicitar ao usuário os valores de entrada
vi = float(input("Digite o valor do investimento inicial: "))
tj = float(input("Digite a taxa de juros anual em porcentagem: "))
p = int(input("Digite o período de investimento em anos: "))

# Calcular o valor do investimento após o período de tempo especificado
vf = vi * (1 + (tj / 100) * p)

# Imprimir o valor do investimento após o período de tempo especificado
print("O valor do investimento após", p, "anos será de R$", vf)