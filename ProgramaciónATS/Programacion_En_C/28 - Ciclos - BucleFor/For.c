/*
Bule for

Sintaxis
for (inicializacion;condicion;incremento){
instrucciones;
....
}


*/

// Ejercicio3 - mostrar 100 veces "No debo llegar tarde" 
#include<stdio.h>
int main(){
    int count;
    for (count=1;count<=100;count++){
        printf("\n%i.No debo llegar tarde",count); // Imprime indicando la cantidad
    }


    return 0;
}










/*
// Ejercicio 1 - mostrar los primeros 10 numeros  - acedente
#include<stdio.h>
int main(){
    int count;
    for (count=1;count<=10;count++){
        printf("%i. \n",count);
    }


    return 0;
}






// Ejercicio2 - mostrar los primeros 10 numeros  - descendente
#include<stdio.h>
int main(){
    int count;
    for (count=10;count>0;count--){
        printf("%i. \n",count);
    }


    return 0;
}


*/