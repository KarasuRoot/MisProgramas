/*
hacer un arbol con '*' del tipo:
Ejemplo Digite el numero de filas: 5
*
**
***
****
*****
*/
#include<stdio.h>
int main(){
int numfilas,count1,count2;  
printf("\nDigite el numero de filas: ");scanf("%i",&numfilas); // aca pido el numero de filas
    for (count1=0;count1<numfilas;count1++){ // con este bucle controlo la cantidad
        for (count2=0;count2<=count1;count2++){ // con este bucle "genero los *"
            printf("*");    
        }
        printf("\n");
    }

    return 0;
}