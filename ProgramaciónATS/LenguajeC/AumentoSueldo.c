/* Calcular el salario de una persona si obtuvo un incremento del 25% sobre su salario anterior.*/
#include<stdio.h>
float salar,aum,salarfinal;
int main(){
    printf("Indique su salario inicial: $");
    scanf("%f",&salar);
    aum = salar * 0.25;
    salarfinal = salar + aum;
    printf ("Su salario con aumento es de: %.2f",salarfinal);

    return 0;
}