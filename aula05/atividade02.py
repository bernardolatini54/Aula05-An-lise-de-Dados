nota = float(input("Nota: "))
frequencia = int(input("Frequência: "))
mensalidade = float(input("Valor da mensalidade: R$ "))

if nota >= 7 and frequencia >= 75:
    bolsa = mensalidade * 0.2
    print(f"Sua nota foi {nota}! Sua frequência foi de {frequencia}%! O valor da bolsa é de R$ {bolsa}.")

else:
    print("Não tem direito à bolsa.")