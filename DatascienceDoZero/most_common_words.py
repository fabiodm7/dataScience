# most_common_words.py
import sys
from collections import Counter

# passa o número de palavras como primeiro argumento
try:
    num_words = int(sys.argv[1])
except:
    print("usage: most_common_words.py num_words")
    sys.exit(1) # código de saída não-zero indica erro

counter = Counter(word.lower() # palavras em minúsculas
                  for line in sys.stdin
                  for word in line.strip().split() # se separam por espaços
                  if word) # pula as palavras vazias

for word,count in counter.most_common(num_words):
    sys.stdout.write(str(count))
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write('\n')