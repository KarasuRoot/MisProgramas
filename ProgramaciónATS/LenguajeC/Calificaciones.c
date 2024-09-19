/* Un alumno desea saber cual sera su calificacion final  en la materia de algoritmos
dicha calificacion se compone de los siguientes porcentajes
55% del promedio de sus tres calificaciones parciales, 30% de la calificacion del examen final y 15% de la calificacion de un trabajo final*/


#include<stdio.h>
float calpar1,calpar2,calpar3,prom_parc,examfinal,prom_examfinal,trabfinal,prom_trabfinal,califfinal;
int main(){
    printf("Indique por favor la calificacion de su 1er calificacion parcial: ");
    scanf("%f",&calpar1);
    printf("Indique por favor la calificacion de su 2da calificacion parcial: ");
    scanf("%f",&calpar2);
    printf("Indique por favor la calificacion de su 3ra calificacion parcial: ");
    scanf("%f",&calpar3);
    printf("Indique por favor la calificacion de su examen final: ");
    scanf("%f",&examfinal);
    printf("Indique por favor la calificacion de su trabajo final: ");
    scanf("%f",&trabfinal);
    prom_parc = ((calpar1+calpar2+calpar3)/3)*0.55;
    prom_examfinal = (examfinal)*0.30;
    prom_trabfinal = (trabfinal)*0.15;
    califfinal= prom_parc+prom_examfinal+prom_trabfinal;
    printf("\nEl promedio de las tres calificaciones es de: %.2f",prom_parc);
    printf("\nEl promedio de su examen final es de: %.2f",prom_examfinal);
    printf("\nEl promedio de su trabajo final es de: %.2f",trabfinal);
    printf("\nSu calificacion final es de: %.2f",califfinal);
    return 0;
}