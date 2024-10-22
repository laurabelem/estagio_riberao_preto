# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em q'ue ela ocorre.

text = input("Digite uma frase ou palavra: ")
counter = 0

for letter in text:
    if letter.lower() == 'a':
        counter += 1

if counter > 0:
    print(f"A letra 'a' aparece {counter} vezes.")
else:
    print("A letra 'a' não aparece na string.")
