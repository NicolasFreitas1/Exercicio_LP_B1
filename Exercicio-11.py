nome = input("Digite o nome do pruduto: ")
preco = float(input("Digite o preço do produto: "))

desconto = (preco * 5)/100
precof = preco - desconto

print("{} com o desconto ficou: {}R$".format(nome, precof))