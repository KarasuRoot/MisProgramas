#Operadores Logicos
'''
Prioridades de los operadores en general:
1 ()
2 **
3 *,/,nidmbit
4 +,-,and
5 >,<,==,>=,<=,!=, or


Permite contruir expreciones logicas y el resultado es booleano

#Operadores

and (podemos tratarlo como una multiplicacion) -- la unica forma que de verdadero es que las dos condiciones sean verdadero
or (conocido como suma logica) -- La unica forma que de Falso es que ambas expresiones sean False
not -- si se niega un resultado Ture da False y viseversa

Prioridade:
NOT
AND
OR
'''

a = 10
b = 12
c = 13
d = 10
resu=((a>b) or (a<c)) and ((a==c) or (a>=b))
print(resu)



