//Tipos de datos en C
#include<stdio.h>
int main(){
    char a = 'e'; //Se almacena en una variable a - el elemento "e" - Tamaño: 1byte Rango:0..255
    short b = -15; // Tamaño = 2bytes Rango -128..127
    int c = 1024; // Tamaño = 2bytes Rango -32768..32767
    unsigned d = 128;// Tamaño = 2bytes Rango ..65535
    long e = 123456; // Tamaño = 4bytes
    float f = 15.678;// Tamaño = 4bytes
    
    double g = 123123.123123;
    printf("El caracter es: %c\n",a); // para imprimir variables tipo char es  %c
    printf("El elemento definido como short es: %i\n",b); // para imprimir variables tipo shot es  %i
    printf("El elemento defindio como int es: %i\n",c); // para imprimir variables tipo shot int  %i
    printf("El elemento defindio como unsigned es: %i\n",d); // para imprimir variables tipo unsigned es  %i - solo enteros positivos
    printf("El elemento defindio como long es: %li\n",e); // para imprimir variables tipo long es  %li - para almacenar datos mas grandes
    printf("El elemento defindio como float es: %f\n",f); // para imprimir variables tipo float es  %f acordarse que podes poner %.2f para que imprima solos los 2 primeros decimales despues de la coma
    printf("El elemento defindio como double es: %lf\n",g); // para imprimir variables tipo double es  %lf - si l ponemos %.lf -> eliminamos la parte decimal, solo imprime entero
    printf("El elemento defindio como double sin decimales es: %.lf\n",g);
    return 0;
}