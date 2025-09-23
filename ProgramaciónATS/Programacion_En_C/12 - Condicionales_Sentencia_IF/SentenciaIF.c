/* 
En programas condicionales, no todo el programa necesariamente se va a ejecutar,
 si usamos If podemos decir q la condicion correcta se va  a ejcutar

La sentencia if:
if (condicion)
    accion
*/

// Ejemplo 1 - Prueba Divisibiidad
#include<stdio.h>
int main(){
    int n1,n2;
    printf("Digite 2 numeros: "); scanf("%i %i",&n1,&n2); // asi es la forma de realizar una entrada de dos datos y guardarlos con scanf
    if (n1 % n2 == 0){ //esta sintaxis es: Si N1 divide por N2 es igual a 0 -- % Encuentra el residuo de la divicion
        printf ("El numero %i es divisible entre %i", n1,n2);
    }

    return 0;
}