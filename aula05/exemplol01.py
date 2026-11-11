valor_pedido = float(input("Digite o valor: "))
distancia = float(input("Distância: "))
frete = 8 

if valor_pedido > 50 and distancia <= 3:
    valor_final = valor_pedido
    mensagem = "Frete grátis."

else:
    frete = 8
    valor_final = valor_pedido + frete
    mensagem = f"Frete de R$ {frete}"

print(mensagem)
print(f"valor final: R$ {valor_final: .2f}")