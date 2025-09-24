/* Seleccionar un tipo de vehiculo e indicar el peaje a agar segun un valor numerico

1 - turismo, peaje = $500
2 - autobus, peaje = $3000
3 - motocicleta, peaje =$300
Caso contrario: Vehiculo no autorizado

*/


#include<stdio.h>


int main(){
    int num;
    printf("Indique un tipo de vehiculo [1 Turismo // 2 Autobus // 3 Motosicleta]: ");
    scanf("%i", &num);
    switch ((num))
    {
        case 1: printf("Su Vehiculo es Tursimo y su peaje correspondiente es $500\n");break; 
        case 2: printf("Su Vehiculo es Autobus y su peaje correspondiente es $3000\n");break;
        case 3: printf("Su Vehiculo Motocicleta y su peaje correspondiente es $300\n");break;
        default: printf("Vehiculo no autorizado\n");break;
    }

    return 0;
}