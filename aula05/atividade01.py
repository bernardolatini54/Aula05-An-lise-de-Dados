nota1 = float(input("Nota da primeira prova: "))
nota2 = float(input("Nota da segunda prova: "))
nota3 = float(input("Nota da terceira prova: "))
nota4 = float(input("Nota da quarta prova: "))

soma = nota1 + nota2 + nota3 + nota4
media_final = soma / 4

if media_final >= 7:
    print(f"Parabéns! Sua média final é {media_final}! Você está APROVADO!")

elif media_final >= 5:
    print(f"Sua média final é {media_final}. Você está em RECUPERAÇÃO.")

else:
    print(f"Sua média final é {media_final}. Você está REPROVADO.")
