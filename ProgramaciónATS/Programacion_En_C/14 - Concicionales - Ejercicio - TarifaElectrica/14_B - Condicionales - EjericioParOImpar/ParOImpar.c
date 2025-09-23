/* Determinar si un numero es par o impar*/
#include<stdio.h>
int main()
{
    int num,resu;
    printf ("Indique un numero: ");scanf("%i",&num);
    resu = num % 2;
    if (resu == 0 )
    {
        printf ("El numero es Par ");
    }
    if (resu != 0) // != no es igual
        printf ("El numero es Impar");
    return 0;
}