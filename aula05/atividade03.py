compra = float(input("Valor da compra: R$ "))
fidelidade = input("Faz parte do programa de fidelidade [S/N]: ").lower()[0] 
frete = 25

if compra > 200:
    valor_final = compra
    mensagem = "Frete Grátis"

elif fidelidade == "S":
    valor_final = compra
    mensagem = "Frete Grátis"

else:
    frete = 25
    valor_final = compra + frete
    mensagem = f"Frete de: R$ {frete}"

print(mensagem)
print(f"Valor final: R$ {valor_final}")