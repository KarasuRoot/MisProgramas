//Lectura y entrada de datos en C++

/* Esta es la forma 
de comentar multiples lineas 
- como en C
*/

#include<iostream>
using namespace std;

int main(){
    int numero;
    cout<<"\nIngrese un numero: ";
    cin>>numero; //asi se guarda el dato solicitado - reempaza el scanf

    cout<<"\nEl numero que ingresso es: "<<numero; //asi se saca por pantalla lo que se guardo en la variable numero y tomado por el cin

    return 0;
}