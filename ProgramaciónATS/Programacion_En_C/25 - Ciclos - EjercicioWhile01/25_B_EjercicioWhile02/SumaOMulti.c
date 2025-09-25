/* Digite un numero, si el numero es mayor a 10 - multiplique los primeros 10 numeros. sino, sumelos*/

#include<stdio.h>
int main(){
    int count,num,sum=0,mul=1;
    printf("Por favor indique la cantidad de numeros que desea: ");scanf("%i",&num);
    count = 1;
    if (num > 10){
        while (count <= num){
        mul = mul*count; 
        count++;
    }
    printf("\nLa multiplicacion es %i",mul);

    }
    else
    {
        while (count <= num){
            sum += count; // aqui va sumando y hacienedo 1 3 6 10 15... tambien puede escribirse asi sum = sum + count;
            count++; // aqui aumenta el contador 1 2 3 4 5
    }
    printf("\nLa suma es %i",sum); // se pone fuera del bucle porq ue queremos que imprima la ultima vez, si qusiera que imprima tdo, debe ser dentro del bucle


    }
    
    return 0;
}