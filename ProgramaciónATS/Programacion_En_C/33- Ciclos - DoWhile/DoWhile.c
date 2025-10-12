/* Repeticion: el bucle do...while
Sintaxis
do{
    instrucciones...
}while(condicion)
- por ejemplo usado para menus
- a diferencia de while - primero ejecuta todas las instrucciones y  luego revisa si se cumple la condicion
Como minimo se ejecuta 1 vez
Luego si se repite, lo sigue haciendo hasta que deje de cumplirse la condicion.

Mostrar los primeros 10 numeros -

#include<stdio.h>
int main(){
    int i=1;
    do
    {
        printf("%i. \n",i);
        i++;
    } while (i<=10);
    
    return 0;
}
*/
#include<stdio.h>
int main(){
    char opc;
    do
    {   
        fflush(stdin); // Limpia la memoria del Buffer
        printf("Hola");
        printf("\nDigite 's' o 'S' para saludar nuevamente ");scanf("%s",&opc);
    } while (opc == 's' || opc == 'S'); // || - es el OR en C -- recordar que && es AND
    
    return 0;
}