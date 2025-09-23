/* Hacer un programa que obtenga la media geometrica de tres numeros*/
#include<stdio.h>
#include<math.h> /* Para realizar la operacion de la potenciacion con "pow"*/
int main(){
    int num1,num2,num3;
    float multi,tot;
    printf ("Indique el primer numero: ");
    scanf("%i" ,&num1);
    printf ("Indique el segundo numero: ");
    scanf("%i" ,&num2);
    printf ("Indique el tercer numero: ");
    scanf("%i" ,&num3);
    multi = num1,num2,num3;
    tot=pow(multi,1.0/3.0);
    printf("La media geometrica es: %.2f\n", tot);
    getchar();
    getchar();
    return 0;
}
