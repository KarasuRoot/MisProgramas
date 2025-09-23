/* Ingrese un numero y calcule e imprima su raiz cuadrada. 
Si el numero es negativo imrimir el numero y un mensaje que diga tiene raiz imaginaria"*/

#include<stdio.h>
#include<math.h>
int main(){
    float num,resu;
    printf ("Indique un numero: ");
    scanf("%f",&num);
    if (num > 0){
        resu = sqrt(num);
        printf("La raiz cuadrada de %.2f es %.2f\n", num, resu);
    } else {
        printf("El numero %.2lf es negativo, por lo tanto tiene raiz imaginaria.\n", num);
    }

    return 0;
}