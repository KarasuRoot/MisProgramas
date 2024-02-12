//Directivas del preprocesador (continene las librerias y macros como por ejemplo #include <stdio.h>) y variables

#include<stdio.h>
#define PI 3.1416 //Esto es una macro la cual tiene como nombre de variable PI y con el valor 3.1416 -> cada vez que se mencion PI -> va a tener un valor asignado (constante)
int y = 5; //Esto es una variable global por que esta fuera de la funcion y puede ser usado en todo el programa
int main(){
    int x = 10; //Se define una variable local (xq esta dentro de una funcion determinada y solo se usa en dicha funcion) de tipo int llamada x y vale 10
    float suma = 0; // Se inicializa la variable en 0 pero tipo Float para que tome los decimales
    //int suma = 0;  -> Se inicializa la variable suma en 0
    suma = PI + x; // Esto va a sumar el valor de PI + el valor de X y lo guarda en la variable suma
    printf("La suma da resultado: %.2f\n",suma); //Se le asigna el tipo de dato con %i y se le asigna el valor de la variable de suma
    /* Esta impresion va a truncar el resultado, solo va a salir la parte entera entonces sera 10+3=13
    el %f es lo mismo que %i nada mas que este es para trabajr con float -> si se le agrega .2 solo imprime hasta dos decimales despues de la coma
    */

    return 0;
}