// Calcular la media artimetica de 3 numeros cualquiera
#include<stdio.h>
int n1, n2, n3,media;

int main(){
    printf("Indique por favor 3 numeros para calcular la media aritmetica: ");
    scanf("%i %i %i",&n1,&n2,&n3) ;
    media=(n1+n2+n3)/3;
    printf("\nLa media de nuestro conjunto de datos es: %i",media);    
    return 0;
    }