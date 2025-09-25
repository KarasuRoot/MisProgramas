/* Sumar pares desde n hasta m*/
#include<stdio.h>
int main(){
    int n1,n2,sum=0;
    printf("\nDigite el numero desde: ");scanf("%i",&n1);
    printf("\nDigite el numero hasta: ");scanf("%i",&n2);
    
    while (n1<=n2)
    {
        if (n1%2==0){
            sum += n1; // es lo mismo que sum_par = sum_par + neg 
        }
        n1++;  
    }
    printf("La Suma es %i ",sum);
    return 0;

}