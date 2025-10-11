/*
Serie Fibonacci
Solictar numero al usuario
Ejemplo 1 1 2 3 5 8 13 ...
*/
#include<stdio.h>
int main(){
    int num, count, x=0,y=1,z=1;
    printf("Digite el numero de elementos ");scanf("%i",&num);
    printf ("1 , ");
    for (count=1;count<num;count++){
        z = x + y; // Calcula el siguiente término de la serie de Fibonacci sumando los dos términos anteriores (x e y).
        x = y;
        y = z;

        printf("%i , ",z);
    }
    


    return 0;
}