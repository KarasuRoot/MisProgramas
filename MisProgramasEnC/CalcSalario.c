/* Dadas las horas trabajadas de una persona y el valor por hora, calcular su salario e imprimirlo*/

#include<stdio.h>
int hor;
float valxhor,salario;
int main(){
    printf("Indique por favor las horas de trabjo que usted realiza: ");
    scanf("%i",&hor);
    printf("Indique por favor su valor por horas trabajadas que usted realiza: $");
    scanf("%f",&valxhor);
    salario = (hor * valxhor);
    printf("\nSu salario es de: $%.2f",salario);
    return 0;
}