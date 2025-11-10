/*
Realizar un programa que lea la entrada estandar de los sigientes datos de una persona
Edad  - Dato de tipo entero
Sexo - Dto de tipo caracter
Altura en metros - Datos de tipo real

Tras leer los datos, el programa debe mostrarlos en la salida estandar

*/

//Mi Version
#include<iostream>
using namespace std;
int main(){
    int edad=0;
    char sexo; // Char solo almacena 1 solo caracter
    double altura=0;

    cout<<"\nPor favor ingrese su Edad: ";cin>>edad;
    cout<<"\nPor favor ingrese su Sexo(M/F): ";cin>>sexo;
    cout<<"\nPor favor ingrese su altura: ";cin>>altura;
    cout << "\nSu edad es " << edad << ", su sexo es " << sexo << " y su altura es " << altura << "." << endl; // de esta forma imprimo todo en una linea
    return 0;
}


/*
Version Alejandro
#include<iostream>
using namespace std;
int main(){
    int edad;
    char sexo[10]; --- esto le da 10 espacios
    float altura;
    cout<<"Digite su edad: ";cin>>edad;
    cout<<"Digite su sexo: ";cin>>sexo;
    cout<<"Digite su altura en metros: ";cin>>altura;
    cout<<"\nEdad: ";cin>>edad;
    cout<<"\nSexo: ";cin>>sexo;
    cout<<"\nAltura:";cin>>altura;
    return 0;
}



*/










/* Mi version 2 - usando el Tipo STRING en la variable sexo
#include<iostream>
using namespace std;
int main(){
    int edad=0;
    string sexo; // permite mas de un caracter
    double altura=0;

    cout<<"\nPor favor ingrese su Edad: ";cin>>edad;
    cout<<"\nPor favor ingrese su Sexo(M/F): ";cin>>sexo;
    cout<<"\nPor favor ingrese su altura: ";cin>>altura;
    cout << "\nSu edad es " << edad << ", su sexo es " << sexo << " y su altura es " << altura << "." << endl; // de esta forma imprimo todo en una linea
    return 0;
}




*/