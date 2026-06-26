print("BEM VINDO AO JOGO DA FORCA")
print("VOCÊ TEM 7 CHANCES PARA ACERTAR A PALAVRA!")
palavra = "Brasil".capitalize()
letra= " "
total_letras= len(set(palavra.lower()))
letras_usuario= []
erros = 0
chances= 7
acertos = 0
while erros < 7 and acertos < total_letras:
    for letra in palavra:
        if letra.lower() in letras_usuario:
            print (letra, end=" ")
        else:
            print ("_", end=" ")
    print ("")
    tentativa= input("Escolha uma letra: ").lower()
    if tentativa in letras_usuario:
        print("VOCE JA JOGOU ESSA LETRA")
        print (f"ESSAS FORAM AS LETRAS QUE VOCE JA REPETIU: {letras_usuario}")
    else:
        letras_usuario.append(tentativa)
        if len(tentativa) !=1:
            print ("DIGITE APENAS UMA LETRA")
        else:
            if not tentativa.isalpha():
                print("DIGITE APENAS LETRAS")
            else:
                if tentativa not in palavra.lower():
                    erros += 1
                    chances -= 1
                    print ("ERROU!")
                    print(f"VOCÊ AINDA TEM {chances} CHANCES! ")
                else:
                    print("ACERTOU!")
                    print(f"VOCÊ AINDA TEM {chances} CHANCES! ")
                    acertos += 1
if erros == 7:
    print("=====VOCE PERDEU A PARTIDA!=====")
    print(f"A PALAVRA ERA {palavra}")
else:
    print(f"=====VOCE GANHOU A PARTIDA!=====")
    print(f"A PALAVRA ERA {palavra}")
