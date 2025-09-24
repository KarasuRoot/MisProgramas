/* 
Hacer un menu que considere las siguientes opciones
caso 1 - cubo de un numero
caso 2 -  numero par o impar
casi 3 - salir
*/

#include <stdio.h>
#include <math.h>

int main() {
    int num, opcion, resu;
    
    printf("Indique un numero: ");
    scanf("%d", &num);
    
    printf("\nElige la opcion que desea");
    printf("\n1 - Elevar su numero al cubo");
    printf("\n2 - Indicar si es Par o Impar");
    printf("\n3 - Salir\n");
    
    printf("\nIndique la opcion: ");
    scanf(" %d", &opcion); // Línea corregida: agregamos un espacio antes del %d
    
    switch (opcion) {
        case 1:
            resu = pow(num, 3.0);
            printf("\nEl numero %d al cubo es %d\n", num, resu);
            break;
        case 2:
            resu = num % 2;
            if (resu == 0) {
                printf("\nEl numero %d es Par\n", num);
            } else {
                printf("\nEl numero %d es Impar\n", num);
            }
            break;
        case 3:
            printf("\nGracias, saliendo\n");
            break;
        default:
            printf("\nOpcion invalida.\n");
            break;
    }
    
    return 0;
}