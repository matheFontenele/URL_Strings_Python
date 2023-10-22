import re

class ExtratorURL():
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
        
# Retira os espaçõs vazios na URL
    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""
    
# Valida se a URl esta vazia
    def valida_url(self):
        if not self.url:
            raise ValueError('A URL esta vazia')
        
# Uso do RegEx para validar se a URL informada tem os padrões exigidos no re.compile 
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError('A URL não é valida')

# Procura a base da URL pelo caracter '?'
    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base
    
# Isola em uma variavel os paramentros da URL
    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros
    
# Busca a informação mda moeda ou valor de acordo com os parametros postados abaixo
    def get_valor_parametro(self, parametros_busca):
        # Busca na URL o '?' e retorna a posição inicial do parametro informado
        indice_parametro = self.get_url_parametros().find(parametros_busca)
        # Retorna o valor somado do indice_paramento mas o tamanho do parametro
        indice_valor = indice_parametro + len(parametros_busca) + 1
        # Busca no parametro se existe '&' faz a validção e retorna o valor em booleano de acordo com o resultado IF
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor
    
# Função para delegar o tamanho do objeto
    def __len__(self):
        return len(self.url)
    
# Transforma o extrator_url em string e concatena varias informações do URL
    def __str__(self):
        return "URL padrão: " + self.url + "\n" "Parametros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

# Sobreescrevendo o metodo __eq__ para qeu possa comparar dois objetos pela url e não pelo endereço de memoria
    def __eq__(self, other):
        return self.url == other.url

#---Fim da Classe Extrator----

url = 'bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real'
extrator_url = ExtratorURL(url)
extrator_url2 = ExtratorURL(url)
valor = extrator_url.get_valor_parametro('quantidade')

print(valor)
print("O tamanho da url é", len(extrator_url))
print(extrator_url)

print(id(extrator_url)) # Metodo ID serve para mostrar o endereço de memoria
print(id(extrator_url2))