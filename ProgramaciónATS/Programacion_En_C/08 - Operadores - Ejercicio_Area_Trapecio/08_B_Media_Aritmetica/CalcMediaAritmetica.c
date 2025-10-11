// Calcular la media artimetica de 3 numeros cualquiera

// Mi Version
#include<stdio.h>
int n1, n2, n3,media;

int main(){
    printf("Indique por favor 3 numeros para calcular la media aritmetica: ");
    scanf("%i %i %i",&n1,&n2,&n3) ;
    media=(n1+n2+n3)/3;
    printf("\nLa media de nuestro conjunto de datos es: %i",media);    
    return 0;
    }

/*
Version Alejandro


#include<stdio.h>

int main(){
	int n1,n2,n3,media_aritmetica=0;
	
	printf("Digite 3 numeros: ");
	scanf("%i %i %i",&n1,&n2,&n3);
	
	media_aritmetica = (n1+n2+n3)/3;
	
	printf("La media aritmetica es: %i",media_aritmetica);
	
	
	return 0;
}
*/