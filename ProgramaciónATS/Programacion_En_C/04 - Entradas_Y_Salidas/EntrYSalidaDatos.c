//Entradas y Salidas de Datos
#include <stdio.h>
int main(){
    /*
    int a= 10;
    float b = 15.5;
    char c = 'e';
    
    printf("%i %.1f %c",a,b,c);  imprimir distintos tipos de variables con un solo printf - cada posicion concuerda con las variables-
    le pone %.1f por que sino imprime 15.500000
    --------------------------------------------------------------------------------
    int d;
    float e;
    char f;
    
    printf("Digite el valor de la variable d: \n"); //aca le pedimos que infrese un digito para almacenarlo en la variable d
    
    scanf("%i",&d); //para tomar lo que tipee el usuario usamos scanf - indicamos que es un entero con %i - luego con &d indica que guarde ese valor en la variable d
    
    printf("El valor ingresado fue: %i",d);
   
    printf("Digite el valor de la variable E: \n"); 
    
    scanf("%f",&e);
   
    printf("El valor ingresado fue: %.1f",e);
    
    printf("Digite el valor de la variable f: \n"); 
    
    scanf("%c",&f);
    
    printf("El valor ingresado fue: %c",f);
    ---------------------------------------------------------------------------------------------
    */
    char x[50]; /*Se define una variable tipo char  con nombre x con un espacio de 50 caracteres*/
    printf("Digite su nombre por favor: ");
    gets(x);
    /* scanf("%s",x);   Se le indica %s para guardar un string - diferencia de %c que solo guarda 1 caracter
    el scanf lee hasta donde encuentra un espacio por ello se reemplaza por gets*/
    printf("Su nombre es: %s",x); 
    return 0;




}