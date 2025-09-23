/* 
Una distribuidora de motocicletas tiene una promocion de fin deaño que consiste:
Las motos de marca Honda tiene un %5 de descuento
las motos de marcha Yamaha tienen un %8 de descuento
las motors de marca Susuki tienen un 10% de descuento
las demas solo un %2 de descuento
Debbe indicar la marca y el precio d la moto
*/
#include<stdio.h>
#include <string.h>
int main(){
	char marca[20];
	float precio,descuento,precioFinal=0;
	
	printf("Digite la marca de su moto: ");
	fgets(marca, sizeof(marca), stdin);
    marca[strcspn(marca, "\n")] = 0;
	printf("Digite el precio de la moto: ");
	scanf("%f",&precio);
	
	if(strcmp(marca,"honda")==0){
		descuento = precio * 0.05;
		precioFinal = precio - descuento;
		printf("El precio final es: %f",precioFinal); 
	}
	else if(strcmp(marca,"yamaha")==0){
		descuento = precio*0.08;
		precioFinal = precio - descuento;
		printf("El precio final es: %f",precioFinal);		
	}
	else if(strcmp(marca,"suzuki")==0){
		descuento = precio*0.1;
		precioFinal = precio-descuento;
		printf("El precio final es: %f",precioFinal);		
	}
	else{
		descuento = precio * 0.02;
		precioFinal = precio - descuento;
		printf("El precio final es: %f",precioFinal);
	}
	
	
	return 0;
}
