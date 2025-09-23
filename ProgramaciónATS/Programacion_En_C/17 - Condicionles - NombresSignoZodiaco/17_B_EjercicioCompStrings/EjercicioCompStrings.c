/* Ingresar por teclado el nombre, la edad y 
el sexo de cualquier persona e imprima, 
solo si la persona es de sexo Masculino y mayor de edad, el nombre de la persona
*/


// Version 3 - Usa scanf y el fgets - el problema de combinarlos es el salto de linea 
#include <stdio.h>
#include <string.h>

int main() {
    char nomb[30], sexo[10];
    int edad;

    printf("Indique su nombre: ");
    fgets(nomb, sizeof(nomb), stdin);
    nomb[strcspn(nomb, "\n")] = '\0';

    printf("Indique su edad: ");
    scanf("%i", &edad);
    getchar(); // Consume el carácter de nueva línea después de scanf()

    printf("Indique Si es Masculino o Femenino: ");
    fgets(sexo, sizeof(sexo), stdin);
    sexo[strcspn(sexo, "\n")] = '\0';

    if (strcmp(sexo, "Masculino") == 0) {
        if (edad >= 18) {
            printf("\nSu nombre es %s, su edad es %i y es de sexo %s", nomb, edad, sexo);
        }
    }
    
    return 0;
}












/* Codigo Verison 1


#include<stdio.h>
#include<string.h>
int main (){
    int edad;
    char nomb[30],sexo[10];
    printf("Indique su nombre: ");
    fgets(nomb, sizeof(nomb), stdin);
    nomb[strcspn(nomb, "\n")] = '\0';
    printf("Indique su edad: ");
    scanf("%i",&edad);
    printf("Indique Si es Masculino o Femenino: ");
    fgets(sexo, sizeof(sexo), stdin);
    sexo[strcspn(sexo, "\n")] = '\0';
    if (stricmp(sexo, "Masculino")==0){
        if (edad > 16){
            printf("\nSu nombre es :%s , su edad es %i y es de sexo %s", nomb, edad, sexo);    
        }
    }
    return 0;
}



==============================================================================================

Version 2 - usa solo el scanf

#include <stdio.h>
#include <string.h>

int main() {
    char nomb[30], sexo[10];
    int edad;

    printf("Indique su nombre: ");
    scanf("%29s", nomb); // Leer nombre sin espacios

    printf("Indique su edad: ");
    scanf("%i", &edad);

    printf("Indique Si es Masculino o Femenino: ");
    scanf(" %9s", sexo); // El espacio antes del %s limpia el buffer de entrada

    if (strcmp(sexo, "Masculino") == 0) {
        if (edad >= 18) {
            printf("\nSu nombre es %s, su edad es %i y es de sexo %s", nomb, edad, sexo);
        }
    }
    
    return 0;
}
*/