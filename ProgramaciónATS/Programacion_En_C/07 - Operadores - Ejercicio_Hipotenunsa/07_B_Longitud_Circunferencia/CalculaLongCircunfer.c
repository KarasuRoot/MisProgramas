// Hacer un programa que calcule la longitudes de la circunferencia
//Mi Version
#include<stdio.h>
#define PI 3.1416
float rad,resul;
int main (){
    printf("Ingrese por favor el diametro para calcular su circunferencia: ");
    scanf("%f",&rad);
    resul= 2*rad*PI;
    printf("La circunferencia del diametro dado es de: %.2f",resul);

}


/*
Version Alejandro

#include<stdio.h>
#define PI 3.1416

int main(){
	float radio,L;
	
	printf("Digite el valor del radio de la circunferencia: ");
	scanf("%f",&radio);
	
	L = PI * radio;
	
	printf("\nLa longitud de circunferencia es: %.2f",L);
	
	
	return 0;
}


*/