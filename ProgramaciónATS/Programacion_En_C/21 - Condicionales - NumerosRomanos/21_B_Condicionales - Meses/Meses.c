/* Mostrar los meses del año, pidiendole al usaurio un numero entre 1 y 12 y mostrar el mes al que corresponde*/
#include<stdio.h>
int main (){
    int mes;
    printf("\nIndique el mes deseado en numero (1-12): ");
    scanf (" %i", &mes);
    switch (mes)
    {
    case 1: printf ("El mes %i seleccionado es Enero\n",mes);break;
    case 2: printf ("El mes %i seleccionado es Febrero\n",mes);break;
    case 3: printf ("El mes %i seleccionado es Marzo\n",mes);break;
    case 4: printf ("El mes %i seleccionado es Mayo\n",mes);break;
    case 5: printf ("El mes %i seleccionado es Abril\n",mes);break;
    case 6: printf ("El mes %i seleccionado es Junio\n",mes);break;
    case 7: printf ("El mes %i seleccionado es Julio\n",mes);break;
    case 8: printf ("El mes %i seleccionado es Agosto\n",mes);break;
    case 9: printf ("El mes %i seleccionado es Septiembre\n",mes);break;
    case 10: printf ("El mes %i seleccionado es Octubre\n",mes);break;
    case 11: printf ("El mes %i seleccionado es Noviembre\n",mes);break;
    case 12: printf ("El mes %i seleccionado es Diciembre\n",mes);break;
    default: printf ("No es un numero valido\n");break;
    }


    return 0;
}