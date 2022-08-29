def get_cidade_pais(cidade,pais,population=''):
    if population:
        cidadePais = cidade + ", " + pais + ' - População: ' + str(population) + '.'
    else:
        cidadePais = cidade + ", " + pais
    return cidadePais.title()
