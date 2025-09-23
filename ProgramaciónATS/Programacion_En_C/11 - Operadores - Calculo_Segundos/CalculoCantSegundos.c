/* Calclar la cantidad de Segundos que estan inlcuidos en el numero de horas, 
minutos y segundos ingresados por el usuario
Es decir el usuario ingresa el numero de horas, minutos y segundos y este ejericcio pretende devolver eal usuario a cantidad de segundos que representa*/
#include<stdio.h>
int main(){
    int horas,minutos,seg,t1,t2,t3,total; //Se declaran las primeras 3 variables por que es lo que requiere que el usuario ingrese, ademas se agregan 3 variables mas para calcular 3 distitnos tiempos y el total de segundos
    printf ('Indique numero de Horas: ');
    scanf('%i' ,&horas);
    printf ('Indique numero de Minutos:');
    scanf('%i' ,&minutos);
    printf ('Indique numero de Segundos: ');
    scanf('%i' ,&seg);
    t1 = horas * 3600; // Para calcular cuantos segundos hay en una hora se multiplica el numero de hora por 3600 - que son 3600 segundos = 1 hora
    t2 = minutos *  60; // Para calcular cuantos segundos hay en un numero de minutos, sabemos que 1 minuto = a 60 segundos
    t3 = seg * 1; // Pacra saber que cantidad de segunod hay sol ose multiplica por 1
    total = t1 + t2 + t3;
    printf('El Equivalente en segundos es: %i', total);
    return 0;
}
