#url = 'bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real'
url =  "     "

#Sanitização da URL
url = url.strip()

#Validação da URl
if url == "":
    raise ValueError("A URL esta vazia")

# Separa base e os parametros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# Busca o valor de um parametro
parametros_busca = 'quantidade'
indice_parametro = url_parametros.find(parametros_busca)
indice_valor = indice_parametro + len(parametros_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor.title())