/*
Suma de los 10 primeros numeros pares
*/

#include<stdio.h>
int main(){
    int contador,sum =0;
    for(contador=0; contador<=10;contador+=2){ //de esta forma es lo mismo que si preguntaramos con if para saber si s par o no 
            sum += contador;
        }
    
printf("\nLa suma de los primeros 10 numeros pares es: %i",sum);


    return 0;
}






/*
Version 1

#include<stdio.h>
int main(){
    int contador,sum =0;
    for(contador=1; contador<=10;contador++){
        if (contador%2==0){ //verificamos si es par - por que lo divide por modulo 2 y si el resto es 0 - es par
            sum += contador;
        }
    }
printf("\nLa suma de los primeros 10 numeros pares es: %i",sum);


    return 0;
}
*/