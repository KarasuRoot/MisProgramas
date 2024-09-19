'''
Una tienda ofrece un descuento del 15% sobre el total de la compra y 
un cliente desea saber cuanto debera pagar finalmente por su compra
'''
precio = float(input('Digite el precio: '))
desc = precio * 0.15
total = precio - desc
print(f'El precio final es de ${total:.2f}')