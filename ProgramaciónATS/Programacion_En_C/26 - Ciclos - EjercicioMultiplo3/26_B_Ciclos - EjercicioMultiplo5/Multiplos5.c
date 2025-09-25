// Multriplos de 5 desde 1 hasta n

#include<stdio.h>
int main(){
    int num,count;
    printf ("\nDigite la cantidad de numeros a comprobar: ");scanf("%i",&num);
    count = 1;
    while (count<=num){
        if (count%5==0) 
        {
            printf("%i. \n",count);
        }
       
        
        count++;
    }
    return 0;
}