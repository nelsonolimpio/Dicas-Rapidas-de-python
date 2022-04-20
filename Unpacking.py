#Unpacking

lista_produtos = [
    ('celular', 1000),
    ('tablet', 1200),
    ('fone de ouvido', 300),
    ('camera', 500),
    ('microfone', 500)

]

for item in lista_produtos:
    produto, preco = item # Unpackimg da tupla.
    print(f"O preço reajustado do {produto} é de {preco * 1.1}")

print("-----------------------------------------------------------")
# Temos uma forma mais simplificada ainda de aplicar o Unpacking no FOR.. Vamos ver abaixo!!!

for produto, preco in lista_produtos:
    print(f"O preço reajustado do {produto} é de {preco * 1.1}")

# Ao dar play no programa, nota-se que o resultados foram exatamente os mesmo, porém, o nosso código ficou mais otimizado. 