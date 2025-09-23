/* Comprobar a traves de un programa si un alumno aprobó o no un examen (Aprueba si la nota es mayor a 10.5)*/
#include<stdio.h>
int main(){
    float examen;
    printf("Indique la nota del examen ") ; scanf("%f",&examen);
    if (examen > 10.5){  // evalua si la nota es mayor a 10.5
        printf("Feliciades, esta aprobado ");
       /* Alternativa para imprimir:
       puts("Feliciadesm esta aprobado ");
       Aclaracion: puts solo imprime dentro de un condicional*/
    }
    return 0;
}