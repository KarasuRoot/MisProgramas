/* Hacer un programa que borre la pantalla al pulsar 1*/

#include<stdio.h>
#include<stdlib.h> // para usar la funcion system(cls)
int main(){
    char tecla;
    printf ("Programa de borrado de pantalla");
    printf("\n------------------------------\n");
    printf("\n------------------------------\n");
    printf("\n------------------------------\n");
    printf("\nDigite el numero 1: ");
    scanf(" %c", &tecla); // Asi es para usar scanf con caracteres
    if (tecla =='1'){ //como comparamos un caracter, eesta con comillas simples
        fflush(stdin); //Limpia el buffer
        system("cls"); //limpia toda la pantalla
        printf("Ha funcionado el limpiado de pantalla");
    }
    else{
        printf("\nNo funciono!!!");
        fflush(stdin); //Limpia el buffer
        printf("\nPor favor digite el numero 1: ");
        scanf(" %c", &tecla);
        
        if (tecla =='1'){ 
            system("cls");
        }
        else{
            printf("No funciono de nuevo!!!");
        }
    }
    return 0;
}