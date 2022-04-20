# List Comprehension

lista_produtos = ['celular', 'tablet', 'fone de ouvido', 'camera', 'microfone']
lista_precos = [1000, 1200, 300, 500, 600]

# Temos a cima, uma lista de preços.
# Mas vamos fazer uma lista de preços com reajustes.

lista_preco_reajuste = [preco * 1.1 for preco in lista_precos]
#Tradução do código a cima: Lista de preços reajustados é igual a preço multiplicado por 1.1, para cada preço da lista_precos.

print(f"Lista de produtos: {lista_produtos}")
print("----------------------------------------------------------------------------------")
print(f"Lista de preços: {lista_precos}")
print("----------------------------------------------------------------------------------")
print(f"Lista de preços com reajustes: {lista_preco_reajuste}")
print("----------------------------------------------------------------------------------")