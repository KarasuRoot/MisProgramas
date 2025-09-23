/* Ingresar por teclado el nombre y el signo de cualquier persona 
e imprima el nombre SOLO si la persona es de signo Aries, caso contrario imrima no es signo Aries*/

#include<stdio.h>
#include <string.h> // Biblioteca para strings - tener en cuenta
int main (){
    char nomb[30],signo[20]; //Asi se definen las variables de tipo CHAR que son strings - el [30] Indica la cantidad de caracteres
    printf("Inidique su nombre: ");
    fgets(nomb, sizeof(nomb), stdin); // Asi se guarda el valor de una variable char/string - tener en cuenta que debe usarse fgets no gets (menos seguro)
    nomb[strcspn(nomb, "\n")] = '\0'; // Eliminar el \n del final del nombre
    printf("Indique su signo: ");
    fgets(signo, sizeof(signo), stdin);
    signo[strcspn(signo, "\n")] = '\0'; // Eliminar el \n del final del signo
    if (stricmp(signo, "Aries") == 0){ /*
        si se indica 0 es que es = a Aries en este caso, si fuera ==1 Preguntaria si es DISTINTO de ARIES
        asi se comparan strings - ademas stricmp no discrimina si es mayus o minusculas*/ 
        printf("\nEs Signo Aries, su nombre es: %s",nomb); // es %s por que es string
    }
    else{
        printf("\nNo es Signo Aries");
    }
    return 0;
}
/*
fgets(signo, sizeof(signo), stdin)
Esta función lee una línea de texto del teclado y la guarda en la variable signo. 
signo: Este es el primer argumento y representa el destino. 
Es el nombre del arreglo de caracteres (o string) donde se va a guardar la entrada del usuario. 
En este caso, es el arreglo llamado signo.

sizeof(signo): Este es el segundo argumento y representa el tamaño máximo. 
Le dice a fgets() cuántos caracteres, como máximo, debe leer. El operador sizeof() calcula automáticamente 
el tamaño total del arreglo signo (que es de 20 bytes). 
Usar sizeof() es la forma más segura de asegurarse de que nunca leerá más caracteres de los que la variable 
puede almacenar. Esto es lo que evita el buffer overflow o desbordamiento de búfer.

stdin: Este es el tercer argumento y representa la fuente. stdin (abreviatura de standard input) 
es un identificador estándar en C que se refiere a la entrada del teclado. 
Le indica a la función que debe leer los datos que el usuario teclee.
*/