/* Suma de los n primeros numeros
como no se sabe cuantos numeros vamos a sumar, se lo preguntamos al usuario
*/

#include<stdio.h>
int main(){
    int count,num,sum=0;
    printf("Por favor indique la cantidad de numeros que desea sumar: ");scanf("%i",&num);
    count = 1;
    while (count <= num){
        sum += count; // aqui va sumando y hacienedo 1 3 6 10 15... tambien puede escribirse asi sum = sum + count;
        count++; // aqui aumenta el contador 1 2 3 4 5
    }
    printf("\nLa suma es %i",sum); // se pone fuera del bucle porq ue queremos que imprima la ultima vez, si qusiera que imprima tdo, debe ser dentro del bucle







    return 0;
}