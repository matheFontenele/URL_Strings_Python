endereco = 'Rua Cuiaba 886, Casa 40, Henrique Jorge, Fortaleza, CE, 60510-188'

import re # Regular Expression -- RegEx

# 5 digitos + hifen (opcional) + 3 digital

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
#OBS: O ? é utilizado para informar que aquele caraacter é opcional no padrão
busca = padrao.search(endereco) # Match - tipo especifico que informa se encontrou ou não o padrao do compile (Retorna Match ou None)
if busca:
    cep = busca.group() # Group - Retorna exatamente a string que foi encontrada naquele padrão
    print(cep)
