import math

Apintada = float(input("Digite o tamanho em metros da área ser pintada: "))

litros = Apintada / 3
lt = math.ceil(litros / 18)  
valor = lt * 80

print(f"Você precisará de {lt} latas de tinta.")
print(f"O valor total a ser pago é R${valor:.2f}")
    


    


    