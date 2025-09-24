/*
La idea es hacer un menú de programa
Hacer un programa que simule un cajero automatico con un saldo inicial de 1000 Dolares
*/

#include<stdio.h>
#define Dinero 1000
int main(){
    int opcion;
    float add,del,tot;
    printf("\t Bienvenido al Cajero Automatico"); // \t en vez de hacer un salto (como lo hace \n) - este deja un espacio de tabulacion
    printf("\n1 - Ingresar Dinero ");
    printf("\n2 - Retirar Dinero ");
    printf("\n3 - Salir");
    printf("\nOpcion: ");
    scanf("%i", &opcion);

    switch (opcion)
    {
    case 1:
        printf("\nIndique la cantidad que desea ingresar en su cuenta");
        scanf("%f",&add );
        tot = Dinero + add;
        printf("\nSu dinero actual es %.2f",tot);break;
    case 2:
        printf("\nIndique la cantidad que desea retirar en su cuenta ");
        scanf("%f",&del );
        if (del > 1000){
            printf("Imposible realizar operacion, Fondos insuficientes");
        }
        else{
        tot = Dinero - del;
        printf("\nSu dinero actual es %.2f",tot);break;
        }
    case 3:
        printf("\nGracias por su visita ");break;
    default:
        printf("\nDigite una opcion correcta ");break;
    }


    return 0;
}