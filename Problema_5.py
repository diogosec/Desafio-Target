palavra = "Target Sistemas"

palavra_invertida = ""

for i in range(len(palavra) - 1, -1, -1):
    palavra_invertida += palavra[i]

print("Palavra original:", palavra)
print("Palavra invertida:", palavra_invertida)