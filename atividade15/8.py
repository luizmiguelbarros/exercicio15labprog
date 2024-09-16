# Solicita o peso dos peixes
peso = float(input("Digite o peso dos peixes em quilos: "))
limite = 50
taxa_multa = 4.00

if peso > limite:
    excesso = peso - limite
    multa = excesso * taxa_multa
    print(f"Quantidade de quilos além do limite: {excesso:.2f} kg")
    print(f"Valor da multa a pagar: R$ {multa:.2f}")
else:
    print("Não há excesso de peso. Nenhuma multa a pagar.")
