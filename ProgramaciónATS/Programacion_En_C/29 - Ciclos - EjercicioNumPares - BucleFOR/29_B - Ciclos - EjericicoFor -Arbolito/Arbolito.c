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
    for (count1=0;count1<numfilas;count1++){ // controlo las filas con este bucle
        for (count2=0;count2<=count1;count2++){ // Controlar los Elementos por Fila
            printf("*");    
        }
        printf("\n");
    }

    return 0;
}

/*
Esta estructura de bucle dentro de bucle es fundamental en programación para trabajar con estructuras bidimensionales
(como matrices o, en este caso, figuras geométricas) donde se necesita una variable para controlar la dimensión principal (las filas)
 y otra para controlar la dimensión secundaria (las columnas o elementos por fila).
*/