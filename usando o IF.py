'''If na mesma linha para situações simples
Bônus do funcionário:
  Se vendeu mais do que 500, o bônus é de R$200
  Se vendeu menos de 500, o bonus é de R$50'''

faturamento = 1000

if faturamento > 500:
    bonus = 200
else:
    bonus = 50
print(bonus)

#A forma a cima seria a forma padrão do python.
#Mas agora vamos usar um único if cujo o unico objetivo desse if é definir o valor de uma variável. Então vamos fazer diferente:

bonus = 200 if faturamento > 500 else 50
# Traduzindo o código a cima: "bonus é igual a 200 se faturamento for maior que 500, se não bonus é igual a 50".
# Essa forma do IF, só é recomendado se for com coisas simples. Como essa citada a cima. 