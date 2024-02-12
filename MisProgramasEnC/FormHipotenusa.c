/* Ejercicio de Hipotenusa de un triangulo
Sacar la hipotenusa de un triangulo rectangulo pidiendo al usuario el valor de dos catetos
*/
#include <stdio.h>
#include <math.h> // se incluye la libreria math para realizar operaciones matematicas, para usar por ejemplo sqrt y pow
float cat1,cat2,resul;
int main(){
    printf("Indique dos valores para los catetos del triangulo rectangulo: ");
    scanf("%f %f",&cat1,&cat2);
    resul = sqrt(pow (cat1,2) + pow(cat2,2)); // sqrt sive para hacer la raiz cuadrada, para usar pow recordar que es (pow (El numero a elevar),el numero del exponente) -> en este ejemplo es el valor ingresado se eleva a la 2
    printf ("La hipotenusa del triangulo rectangulo es: %.2f",resul);
    return 0;
}