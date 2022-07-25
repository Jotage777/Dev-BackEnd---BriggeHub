import re

def validar_nome(nome):
    validar = '^[ a-zA-Z á]*$'
    if (re.search(validar, nome)):
        return True
    else:
        return False


def validar_email(email):
    validar = '[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]'
    if (re.search(validar, email)):
        return True
    else:
        return False

def valida_telefone(telefone):
    padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
    resposta = re.findall(padrao, telefone)
    if resposta:
        return True
    else:
        return False