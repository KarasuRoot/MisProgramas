/* Hacer un programa que calcule la suma de factoriales 
1 - Calcular el factorial de uno o más números (o de una serie de números).
2 - Sumar esos resultados factoriales.


Por ejemplo, si el usuario introduce N=4, el programa debe calcular:
Suma=1!+2!+3!+4!

Donde:

    1!=1

    2!=2×1=2

    3!=3×2×1=6

    4!=4×3×2×1=24

Por lo tanto:
Suma=1+2+6+24=33

*/


#include<stdio.h>
int main()
{
    int num,count,facto=1,sumfac=0; // se inicializa en uno por que es una multiplicacion - todo lo multiplicado por 0 da 0
    printf("\nDigite un numero para realizar la operacion factorial: ",num);scanf("%i",&num);
    for (count=1;count<=num;count++){
        facto *= count; //para recorrer el bucle y realizar la multiplicacion con cada numero 
        sumfac += facto;
    }
    printf("\nEl factorial del numero dado es: %i",facto);
    printf("\nLa Suma es: %i",sumfac);
    return 0;
}



/* 
Version Alejandro

#include<stdio.h>

int main(){
	int factorial = 1, suma = 0,i,n;
	
	printf("Digite la cantidad de factoriales a sumar: ");
	scanf("%i",&n);
	
	for(i=1;i<=n;i++){
		factorial *= i;
		suma += factorial;		
	}
	
	printf("La suma es: %i",suma);
	
	return 0;
}
*/