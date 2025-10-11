/*
Hacer un programa que imprima la suma de todos los numeros pares que hay desde 1 hasta N y diga cuantos numeros hay
*/
#include<stdio.h>
int main(){
    int i,num,sumpar=0,contapar=0;
    printf("Indique un numero: ");scanf("%i",&num);
     for(i=2; i<=num;i+=2){  
            sumpar += i; //Es una forma corta de decir sumpar = sumpar + i;Añade el número par actual (i) a la suma total que se está acumulando en la variable sumpar.
            contapar++; //Es una forma corta de decir contapar = contapar + 1;Cada vez que el bucle encuentra un número par y lo suma, aumenta este contador en 1, cumpliendo la parte de la tarea que pide "decir cuántos números hay".
        }
    printf("\nLa suma de los pares hasta %i es: %i\n", num, sumpar);
    printf("El numero de elementos pares es: %i\n", contapar);
    return 0;
}



/*
Version Alejandro

#include<stdio.h>

int main(){
	int cont=0,i,suma=0,n;
	
	printf("Digite la cantidad de elementos: ");
	scanf("%i",&n);
	
	for(i=1;i<=n;i++){
		if(i%2==0){
			suma += i;
			cont++;
		}
	}
	
	printf("\n La suma es: %i",suma);
	printf("\n La cantidad de numeros es: %i",cont);
	
	
	
	return 0;
}




*/