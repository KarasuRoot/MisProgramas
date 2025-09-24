/* Sentencia switch () - Condicional Multiple

switch (Selector) { --> el selector es una variable SOLO de tipo entero o char

case etiqueta1 : sentencia1;break;
case etiqueta2 : sentencia2;break;
case etiqueta3 : sentencia3;break;
default: sentencias;

}*/


/* Ejemplo de las vocales Version 2.0 --  
En la version anterior, si ponia A me tomaba sin problemas la vocal, pero si ponia a no - porque es sencible a las minuscualas y mayusuclas



*/

#include<stdio.h>
#include <ctype.h> // Esta biblioteca contiene un conjunto de funciones muy útiles para clasificar y transformar caracteres.

int main(){
    char vovcal;
    printf("Digite una vocal (A // E // I // O // U): ");
    scanf(" %C", &vovcal);
    switch (toupper(vovcal)) // toupper [Para mayusculas] // tolower [Para minusuclas] - convierte en este caso lo que teclee en Mayusuclas por usar toupper
        {
        case 'A': printf("Usted eligio la letra A\n");break; // A diferencia del otro ejemplo el case cuando lleva caracter va entre ' '
        case 'E': printf("Usted eligio la letra E\n");break;
        case 'I': printf("Usted eligio la letra I\n");break;
        case 'O': printf("Usted eligio la letra O\n");break;
        case 'U': printf("Usted eligio la letra U\n");break;
        default: printf("No es una Vocal \n");break;
    }

    return 0;
}



/*
Ejemplo1 - Ejemplo del Numero 

#include<stdio.h>


int main(){
    int num;
    printf("Digite un numero entre 1-3: ");
    scanf("%i", &num);
    switch ((num))
    {
        case 1: printf("Usted eligio el numero 1\n");break; // el Break finaliza la isntruccion evitando asi se ejecuten otras sentencias
        case 2: printf("Usted eligio el numero 2\n");break;
        case 3: printf("Usted eligio el numero 3\n");break;
        default: printf("No a digitado un numero correcto \n");break;
    }

    return 0;
}


// Ejemplo2  de las vocales -- 

#include<stdio.h>


int main(){
    char vovcal;
    printf("Digite una vocal (A // E // I // O // U): ");
    scanf("%C", &vovcal);
    switch ((vovcal))
    {
        case 'A': printf("Usted eligio la letra A\n");break; // A diferencia del otro ejemplo el case cuando lleva caracter va entre ' '
        case 'E': printf("Usted eligio la letra E\n");break;
        case 'I': printf("Usted eligio la letra I\n");break;
        case 'O': printf("Usted eligio la letra O\n");break;
        case 'U': printf("Usted eligio la letra U\n");break;
        default: printf("No es una Vocal \n");break;
    }

    return 0;
}








*/