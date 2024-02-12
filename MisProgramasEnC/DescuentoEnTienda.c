/* Una tienda ofrece un descuento del 15% sobre el total de la compra
y un cliente desea saber cuatno debe pagar finalmente por su compra*/

#include<stdio.h>
int main(){
    float total_com,desc,precio;
    printf("Indique el total de compra: $");
    scanf("%f",&total_com);
    desc = total_com * 0.15;
    precio = total_com - desc;
    printf("\nEl precio final de su compra es: $%.2f",precio);
    return 0;
}