import random

palavra = 'vasco'

palavra_rand = list(palavra)
random.shuffle(palavra_rand)

palavra_rand = "".join(palavra_rand)

frases = ["Tente novamente", "Você consegue ;)"]
print(f"Palavra embaralhada: {palavra_rand}\n")
contador = 0
while contador < 5:
    contador +=1
    print(f"tentativa {contador}")
    resposta = input("tente: ")

    if resposta == palavra:
        print("parabens, acertou")
        break

    frase = random.choice(frases)
    print(frase)
print(f"você teve {contador} tentativas")

        