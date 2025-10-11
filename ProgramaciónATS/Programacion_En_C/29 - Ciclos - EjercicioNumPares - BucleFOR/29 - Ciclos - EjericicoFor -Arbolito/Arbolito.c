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
printf("\nDigite el numero de filas: ");scanf("%i",&numfilas);
    for (count1=0;count1<numfilas;count1++){
        for (count2=0;count2<=count1;count2++){
            printf("*");    
        }
        printf("\n");
    }

    return 0;
}