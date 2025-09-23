/*
Operaciones aritmeticas
Pedir 2 numeros al usuario, sumarlos, restarlos y dividirlos

*/
#include<stdio.h>
int main (){
    int n1,n2, suma = 0, resta = 0, mult = 0, div = 0;
    /* printf("Digite el primer numero: ");
    scanf("%i,&n1");
    printf("Digite el segundo numero: ");
    scanf("%i,&n2");
    esta es una forma de pedir que digite dos numeros y guardarlos en dos variables distinas
    */ 
    printf ("Digite los dos numeros para las operatorias aritmeticas: ");
    scanf("%i %i",&n1,&n2);
    suma = n1 + n2;
    resta = n1 - n2;
    mult = n1 * n2;
    div = n1 / n2;
    printf ("\nLa suma de sus dos numeros es: %i",suma);
    printf ("\nLa resta de sus dos numeros es: %i",resta);
    printf ("\nLa multiplicacion de sus dos numeros es: %i",mult);
    printf ("\nLa divicion de sus dos numeros es: %i",div);
    return 0;
}