faturamento = 1000000000
texto_faturamento = f"{faturamento:,.2f}".replace(",","_").replace(".",",").replace("_",".")
print(f"O faturamento foi de R${texto_faturamento}")

# Para facilitar esse processo, o Python tem uma biblioteca padrão que ja vem instalada no próprio Python.
# Essa biblioteca é a biblioteca "locale", ela permite você adaptar várias coisas ao formato local, como Data, número, etc...
# formato local (BRASIL). -------->

#Vamos então importar essa biblioteca com o comando abaixo:

import locale

#Com a biblioteca importada, como vamos definir o local em que estamos? (Brasil, EUA, Austrália, Espanha etc...)
#Vamos rodar o código abaixo:

locale.setlocale(locale.LC_ALL, '')

# O comando a cima, define o que queremos adaptar... Se quisermos adaptar somente mensagens, por exemplo, vamos usar LC_MESSAGES.
# Se quisermos adaptar somente os caracters numéricos, por exemplo, vamos usar o comando LC_NUMERIC.
# No caso do comando a cima, nós vamos adaptar TODAS as opções.
# Logo depois de definir o que queremos adaptar, nós vamos falar para o Python que queremos o Portguês do BRASIL usando o comando 'pt_BR.UTF-8'.
# Se o código a cima der erro, podemos usar o comando 'Portuguese_Brazil.1252'.
# Vamos definir o local nos comandos abaixo (Assim como foi explicado a cima):

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Agora vamos criar uma outra variável para que possamos trabalhar o comando locale, em cima dela.

texto_faturamento2 = locale.currency(faturamento, grouping=True)
# O comando a cima, vai pegar a variável faturamento, passar ela para o formato de currency (moeda) usando as informações padroes locais do Brasil.
# O comando grouping=True, ele vai agrupar os números usando o separador de milhar.
# Vamos imprimir pra ver se realmente deu certo?

print('------------------------------------------')
print(f"O faturamento foi de {texto_faturamento2}")

# Pode-se obervar que ao imprimir o código a cima, ele automaticamente ja deu o R$.
# Para desativar o símbolo R$, basta usar o comando symbol=false logo após a virgula. Como no exemplo abaixo.
'''--------------------------------------------------------------------------------------------------------------'''
#texto_faturamento2 =  locale.currency(faturamento, grouping=true, symbol=False)

