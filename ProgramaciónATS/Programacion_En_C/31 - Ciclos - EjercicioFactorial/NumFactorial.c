/*
Factirual de un numero
El usuario ingresrara un numero
Luego el programa deberá realizar la multiplicacion sucesiva - ejemplo:
Si ingreso 5 - debe hacer 1x2x3x4x5

*/

#include<stdio.h>
int main()
{
    int num,count,facto=1; // se inicializa en uno por que es una multiplicacion - todo lo multiplicado por 0 da 0
    printf("\nDigite un numero para realizar la operacion factorial: ",num);scanf("%i",&num);
    for (count=1;count<=num;count++){
        facto *= count; //para recorrer el bucle y realizar la multiplicacion con cada numero 
    }
    printf("\nEl factorial del numero dado es: %i",facto);
    return 0;
}
