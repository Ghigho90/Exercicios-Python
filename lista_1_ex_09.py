tot = float(input("Digite o valor total da compra: "))
percentual_desconto = float(input("Digite o percentual de desconto a ser aplicado: "))

desc = tot * (percentual_desconto / 100)
vf = tot - desc

print("O valor do desconto é:", desc)
print("O valor final da compra com o desconto aplicado é:", vf)