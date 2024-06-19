#Operadores aritmeticos
num1 = 10
num2 = 5
suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
div = num1 / num2 #recordar que tenemos como resultado un flotante
div2 = num1 // num2 #con '//' da el resultado con la parte entera (hacia abajo)
modulo = num1 % num2 #devuelve el reciduo o resto de la divicion.
expo = num1 ** num2
print('El resultado de la suma es ',suma)
print('El resultado de la resta es ',resta)
print('El resultado de la multiplicacion es ',multi)
print('El resultado de la divicion es ',div)
print('El resultado de la divicion con parte entera es ',div2)
print('El resultado del resto de la divicion es es ',modulo)
print('El resultado del exponenete es ',expo)

'''Reglas de precedencia
Parentesis
Exponentes
Multiplicacion y Divicion
Suma y resta
'''

# Ejemplo 1: Operaciones aritméticas

resultado = 2 + 3 * 4 # Multiplicación antes que suma

print(resultado)  # Resultado: 14

# Ejemplo 2: Paréntesis

resultado = (2 + 3) * 4 # Paréntesis antes que multiplicación

print(resultado)  # Resultado: 20

# Ejemplo 3: Exponentes

resultado = 2 ** 3 + 4 # Exponente antes que suma

print(resultado)  # Resultado: 10

# Ejemplo 4: Operadores lógicos

resultado = (True and False) or not True # And antes que Or, not antes que and

print(resultado)  # Resultado: False