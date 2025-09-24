/*Sentencia if de dos altenativas: if-else -Condicional Doble
if (condicion)
    accion 1
else -- si no se cumple, salta aqui
    accion 2
*/
// Nota del estudiante
#include<stdio.h>
int main(){
    float nota;
    printf("Digite la nota del examen ");scanf("%f",&nota);
    if (nota >10.5){
        printf("Alumno Aprobado ");
    }
    else{
        printf("Alumno Desaprobado");
    }  
    
    return 0;
}
    

