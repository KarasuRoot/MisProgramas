/*
Escribe un programa que lea de la entrada estandar dos numeros 
y muestre en la salida estandar su suma, resta, multiplicacion y divicion
*/

#include<iostream>
using namespace std;
int main(){
    int num1, num2, sum=0, res=0, mul=0, div=0;
    cout<<"Digite el primer numero: ";cin>>num1;
    cout<<"Digite el segundo numero: ";cin>>num2;
    sum = num1 + num2;
    res = num1 - num2;
    mul = num1 * num2;
    div = num1 / num2;
    cout<<"\nLa suma es: "<<sum<<endl;
    cout<<"La resta es: "<<res<<endl;
    cout<<"La multiplicacion es: "<<mul<<endl;
    cout<<"La divicion es: "<<div<<endl;
    return 0;
}