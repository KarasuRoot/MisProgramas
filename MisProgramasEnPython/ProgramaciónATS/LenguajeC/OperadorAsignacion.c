// Operador de Asignación
#include<stdio.h>
int main(){
    int a,b,c;
    a = 10;
    /* a +=10;  es lo mismo que hacer a = a + 10
    a = b = c = 10;  el = es el operador de asignacion y asi puedo asignar a las 3 variables el 10
    a -=5;  es lo mismo que la suma, solo que resta 5
    a *=2; es lo mismo pero multiplica x2 */
    a /=2; //es lo mismo pero divde x2

    printf("El valor de a es: %i",a);
    return 0;
}