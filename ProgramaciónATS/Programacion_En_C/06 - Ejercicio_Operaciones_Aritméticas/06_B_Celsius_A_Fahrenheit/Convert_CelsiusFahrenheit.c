// Convertir grados celcius en Fahrenheit

// Mi Version
#include<stdio.h>
float Celc,Fha;
int main(){
    printf ("Ingrese el Grado Celsius a convertir en Grados Fahrenheit: ");
    scanf("%f",&Celc);
    Fha = (Celc * 9/5) + 32;
    printf ("La conversion de Grados Celcius a Fhrenheit es: %.2f",Fha);
    return 0;
}



/*
Version Alejandro

#include<stdio.h>

int main(){
	float grados_celsius,grados_f;
	
	printf("Digite los grados Celsius: ");
	scanf("%f",&grados_celsius);
	
	grados_f = grados_celsius * 1.8 +32;
	
	printf("\nEl equivalente en Grados Fahrenheit es: %f",grados_f);
	
	
	return 0;
}


*/