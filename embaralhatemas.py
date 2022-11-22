import random

temas = {
    "Fruta": {
        "Facil": ['maça','pera','caju'],
        "Medio": ['banana','manga','laranja'],
        "Dificil": ['melancia','abacaxi','pitaia']
    },
    "Cor": {
        "Facil": ['azul','rosa','preto'],
        "Medio": ['branco','marrom','verde'],
        "Dificil": ['laranja','vermelho','azul-calcinha']
    },
    "Times": {
        "Facil": ['vasco','bangu','ajax'],
        "Medio": ['joinville','criciuma','tubarao'],
        "Dificil": ['real madrid','corinthian','athletico paranaense']
    }
}

print(list(temas.keys()))

tema = input("Escolha o tema: ")
print(list(temas['Fruta'].keys()))
dificuldade = input("Escolha a dificuldade: ")

palavras = (temas[tema][dificuldade])

palavra = random.choice(palavras)

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

        