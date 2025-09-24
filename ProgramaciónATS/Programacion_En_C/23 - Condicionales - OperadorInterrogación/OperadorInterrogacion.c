/* Operador Interrogacion (?)
Expresion condicional
Sintaxis:
Condicion ? Expresion1: Expresion2 
Otra forma de ver si es par o no
*/

#include<stdio.h>
int main(){

    int numero;
    printf("Digite un numero ");
    scanf("%i",&numero);
    (numero%2==0) ? printf("El Numero es par") : printf ("El numero es impar"); //Si la condicion (numero%2==0) es verdadera, ejecuta el primer termino antes del : sino ejecuta el segundo
    /*
    (numero%2==0) ? Bloque Funcion1 : Bloque Funcion2; -- usualmente esto se usa asi para ejecutar dsitinas funciones segun se cumpla una condicion
    */
    return 0;
}