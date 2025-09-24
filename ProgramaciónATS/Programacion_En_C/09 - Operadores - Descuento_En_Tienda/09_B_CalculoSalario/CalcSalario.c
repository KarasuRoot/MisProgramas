/* Dadas las horas trabajadas de una persona y el valor por hora, calcular su salario e imprimirlo*/

#include<stdio.h>
int hor;
float valxhor,salario;
int main(){
    printf("Indique por favor las horas de trabjo que usted realiza: ");
    scanf("%i",&hor);
    printf("Indique por favor su valor por horas trabajadas que usted realiza: $");
    scanf("%f",&valxhor);
    salario = (hor * valxhor);
    printf("\nSu salario es de: $%.2f",salario);
    printf("\nPrecione Enter para salir...");
    getchar();
    getchar(); /* Se usa x2 getchar() -> Cuando ingresas el valor de las horas o del salario, escribes un número y luego presionas la tecla Enter. La función scanf() lee el número, pero deja el carácter de nueva línea (\n) que produce la tecla Enter en el búfer de entrada.

Cuando pones solo un getchar() después de printf("\n\nPresione cualquier tecla para salir...");, ese getchar() lee inmediatamente ese carácter de \n que quedó pendiente. Como el getchar() ya "leyó" algo, el programa asume que la entrada se ha completado y continúa, lo que provoca que se cierre la ventana de la consola.

El segundo getchar() es el que realmente espera a que presiones una tecla para continuar y, por lo tanto, mantiene la ventana abierta hasta que lo haces.*/
    return 0;
}