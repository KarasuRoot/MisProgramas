/* Visualizar la tarifa de la luz segun el gasto de corriente electrica. 
Para un gasto MENOR de 1.000Kwxh la tarifa es 1.2
Entre 1.000y  1.850Kwxh es 1.0
y si es mayor de 1.850Kwxh 0.9*/
#include<stdio.h>
#define TARIFA1 1.2
#define TARIFA2 1.0
#define TARIFA3 0.9
int main(){
    float gasto,pago;
    printf("Digite el total de gasto de energia ");
    scanf ("%f",&gasto);
    if (gasto < 1000){ // gasto es menor a 1000
        pago =TARIFA1;
    }
    if (gasto > 1000 && gasto < 1850){ // el && es el AND(Y) en C
       pago = TARIFA2;
    }
    if (gasto > 1850){ //gasto mayor a 1850
        pago = TARIFA3;
    }
    printf("La tasa a pagar es: %.1f ",pago);
    return 0;
}
