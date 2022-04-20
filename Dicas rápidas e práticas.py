

faturamento = 1000000000 #Declarando a variável faturamento.
texto_faturamento = f"{faturamento:,.2f}".replace(",","_").replace(".", ",").replace("_",".")

# A cima nós declaramos a variável texto_faturamento, porém usamos o comando replace, que configura a variável da maneira que desejamos.
#o primeiro replace .replace(",","_") eu estou trocando todas as vírgulas por anderlines, pois o anderline em python separa as centenas.
# logo em seguida vamos converter todos os pontos em vírgulas .replace(".",",").
# e o ultimo replace vamos converter todos os anderlines em pontos .replace("_",".").
# VAMOS VER O QUE VAI DAR?????????

# Abaixo vamos expor passo a passo. (Depois de declarar as variáveis).

print(f"O faturamento foi de {faturamento}") #estamos utilizando a variável faturamento.
# A letra "f" antes da frase significa que ele automaticamente vai imprimir a variável basta colocar entre {} o nome da variável.
print("___________________________________________")

print(f"O faturamento foi de R${faturamento:,}")
# Os dois pontos no final do nome da variável significa que você quer formatar a variável para um valor de moeda.
# a virgula é o separador de milhar.
print("___________________________________________")

print(f"O faturamento foi de R${faturamento:,.2f}")
# o ponto diz que queremos o separador decimal. Números depois da vírgula.
# E logo em seguida nós colocamos a quantidade de casa que queremos depois da vígula. Neste caso 2 casas (2f) {F de float).
# VAMOS VER COMO VAI FICAR?
print("___________________________________________")

print(f"O faturamento foi de R${texto_faturamento}")
print("desta vez com as configurações de valores em REAL brasileiro.")
# dessa vez nós vamos utilizar a variável texto_faturamento com todas as configurações do replace.
print("___________________________________________")
