/* Dada una nota  de un examen mediante un codigo, escribir el literal que le corresponde a la nota

A - Excelente
B - Notable
C - Aprobado
D y F - Reprobado

*/

//Mi version

#include<stdio.h>
#include <ctype.h>

int main(){
    char nota;
    printf("Indique la nota del Alumno (A/B/C/D/F): ");
    scanf(" %C", &nota);
    switch (toupper(nota)) {
        case 'A': printf("El alumno a sacado una Exelente Nota\n");break; 
        case 'B': printf("El alumno a sacado una Notable Nota\n");break;
        case 'C': printf("El alumno Aprobo \n");break;
        case 'D': 
        case 'F': printf("El alumno reprobo\n");break;
        default: printf("No es una nota Correcta \n");break;
    }

    return 0;
}





/*
Version del video

#include<stdio.h>


int main(){
    char nota;
    printf("Digite la Nota: ");
    scanf(" %C", &nota);
    switch ((nota)) {
        case 'A': printf("Exelente\n");break; 
        case 'B': printf("Notable\n");break;
        case 'C': printf("Aprobo \n");break;
        case 'D': 
        case 'F': printf("Reprobo\n");break;
        default: printf("Se equivoco de  nota\n");break;
    }

    return 0;
}



*/