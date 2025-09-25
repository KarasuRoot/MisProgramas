/* Sentencia While (Mientras que) - seguira repitiendo la accion hasta que la condicion dejen de cumplirse
While se usa cuando  conocemos  una condicion determinada que queremos que se cumpla
Sintaxis: while (condicion){
            instruciones;
            }
*/
// Mostrar 5 asteriscos "*"



#include<stdio.h>
int main(){
    int count; 
    count = 1; 
    while (count <= 5)  
    {
        printf("*"); 
        count++;
    

    }
    


    return 0;
}       



/*
     // Ejemplo: mostrar los primeros 10 numeros en pantalla de forma ascendente

#include<stdio.h>
int main(){
    int count; //la variable count  es el iterador, la variable de conteo
    count = 1; //se debe inicializar la variable en C       
    while (count <= 10) //la condicion es que mientras count sea menor o igual a 10
    {
        printf("%i \n",count); //imprime el valor que tenga la variable count
        count++;//incrementa la variable - puede ser tambien como count = count+1 // o tambien puede ser  count +=1 // y para cuando solo se suma 1 solo count++

    }
    


    return 0;
}       



// Ejemplo mostrar los primeros 10 numeros en pantalla de forma descendente

#include<stdio.h>
int main(){
    int count; 
    count = 10; 
    while (count > 0)  // tambien segun el video podria ser while (i>=1)
    {
        printf("%i \n",count); 
        count--; //decrementa 1 en 1
    

    }
    


    return 0;
}       
            
*/