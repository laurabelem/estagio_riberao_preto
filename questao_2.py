text = input("Digite uma frase ou palavra: ")
counter = 0

for letter in text:
    if letter.lower() == 'a':
        counter += 1

if counter > 0:
    print(f"A letra 'a' aparece {counter} vezes.")
else:
    print("A letra 'a' não aparece na string.")
