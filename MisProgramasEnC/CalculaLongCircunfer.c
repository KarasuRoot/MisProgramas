// Hacer un programa que calcule la longitudes de la circunferencia
#include<stdio.h>
#define PI 3.1416
float rad,resul;
int main (){
    printf("Ingrese por favor el diametro para calcular su circunferencia: ");
    scanf("%f",&rad);
    resul= 2*rad*PI;
    printf("La circunferencia del diametro dado es de: %.2f",resul);

}