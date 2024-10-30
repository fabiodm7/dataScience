# egrep.py
import sys,re

# sys.argv é a lista dos argumentos da linha de comando
# sys.argv[0] é o nome do programa em si
# sys.argv[1] será o regex especificado na linhas de comando
regex = sys.argv[1]

# para cada linha passada pelo script
for line in sys.stdin:
    # se combinar com o regex, escreva-o para o stdout
    if re.search(regex,line):
        sys.stdout.write(line)
