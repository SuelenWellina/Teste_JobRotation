
print("--- Iverção de palavras ---")

# Recebendo os dados
palavra = input("Digite uma palavra:")

# Vetor que vai receber as palavras
caracteres = []

# Variavel que recebe a palavra invertida
invertido = ''

# Conta cada letra da palavra
for letra in palavra:
    # Salva a letra no vetor de caracteres
    caracteres.append(letra)

# Salva o tamanho do vetor (quantidade de letras) menos 1 para usar como base para o próximo repetição.
tam = len(caracteres) - 1

# Repete o vetor de caracteres de forma inversa e salva cada caractere na String invertida.
while tam >= 0:
    invertido += (caracteres[tam])
    tam -= 1

print("Palavra invertida: ")
print(invertido)