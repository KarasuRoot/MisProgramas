/* Calcular el mayor de dos numeros leidos del teclado y visualizarlo en pantalla*/
#include<stdio.h>

int main(){
    int n1,n2;
    printf("Indicar los dos numeros: ");
    scanf("%i %i",&n1,&n2);
    if (n1>n2){
        printf ("\nEl Mayor es: %i",n1);
    }
    else if (n2 > n1){ //Condicional anidado - es decir un condicional, dentro de otro
        printf ("\nEl mayor es: %i" ,n2);
    }
    else {
        printf ("\nAmbos numeros son iguales");
    }    
    
    return 0;
}