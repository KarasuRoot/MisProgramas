// Convertir grados celcius en Fahrenheit
#include<stdio.h>
float Celc,Fha;
int main(){
    printf ("Ingrese el Grado Celsius a convertir en Grados Fahrenheit: ");
    scanf("%f",&Celc);
    Fha = (Celc * 9/5) + 32;
    printf ("La conversion de Grados Celcius a Fhrenheit es: %.2f",Fha);
    return 0;
}