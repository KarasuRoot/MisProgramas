/*
Hacer un bucle do... while para imprimir las letras minisculas del alfabeto

*/

#include<stdio.h>
int main(){
    char letra ='a'; //los char en realdiad guardan valos ASCII - esto quiere decir que esta guardando 61h (hexadecimal)
    do
    {
        printf ("%c. \n",letra);
        letra++;
    } while (letra<='z');
    
    return 0;
}