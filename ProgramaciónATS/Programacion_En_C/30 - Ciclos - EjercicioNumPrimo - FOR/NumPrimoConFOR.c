/*
Determinar si un numero es primo o no
*/
#include<stdio.h>
int main(){
    int count, num, conta=0;
    printf("Digite un numero: ");scanf("%i",&num);
    for (count=1;count<=num;count++){
        if (num%count==0){
            conta++;

        }
    }
    if (conta>2){
        printf("\n El numero %i es compuesto",num);
    }
    else{
        printf("\n El numero %i es primo",num);
    }    
    return 0;
}