/* Comrpobar si un nuemero digitqado por el usuario es Positivo o Negativo */
#include<stdio.h>
int main(){
    int num;
    printf("Digite su numero: "); scanf("%i",&num);
    if (num > 0){
        printf("Su numero es positivo ");
    }
    else{
        printf ("Su numro es negativo");
    }
return 0;
}