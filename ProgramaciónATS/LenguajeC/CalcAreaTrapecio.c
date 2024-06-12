//Hacer un programa que calcule areas de trapecios
#include<stdio.h>
int main(){
    float base_men,Base_May,area,altur;
    printf("Ingrese la base mayor: ");
    scanf("%f",&Base_May);
    printf("Ingrese la base menor: ");
    scanf("%f",&base_men);
    printf("Ingrese la altura: ");
    scanf("%f",&altur);
    area = ((Base_May+base_men)*altur)/2;
    printf("\nEl area del trapecio es: %.2f",area);

    return 0;
}