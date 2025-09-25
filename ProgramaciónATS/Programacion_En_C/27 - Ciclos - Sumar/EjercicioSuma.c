/* Sumar 1-2+3-4...n
Notas: 
numeros impares (+) -- si nos fijamos bien los impares son todos +
numeros pares (-) -- mientras que los pares son todos -
entonces tendremos:
sum_par
sum_imp
sum = sum_par + sum_imp
1-2+3-4+5-6
-1+3-4+5-6
2-4+5-6
-2+5-6
3-6
-3


*/
#include<stdio.h>
int main(){
    int count,num,sum=0,sum_par=0,sum_imp=0,neg; // la variable neg es para trasnformar los numeros pares en negativos
    printf("\nDigite el numero total de elementos a sumar: ");scanf("%i",&num);
    count = 1;
    while (count<=num)
    {
        if (count%2==0){
            neg = count*(-1); // asi se transforman los pares en negativos
            sum_par += neg; // es lo mismo que sum_par = sum_par + neg
        }
        else{
            sum_imp += count;
        }
        count++;
    }
    sum =sum_imp+sum_par;
    printf("\nLa Suma total es %i",sum);

    return 0;
}