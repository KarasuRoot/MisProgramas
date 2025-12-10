/*
Escribe la siguiente expresion matematica como una expresion en C++
A/B +1 (a sobre b más uno)
*/

#include<iostream>
using namespace std;
int main(){
    float a,b,result=0;
    cout<<"Digite el valor de A: ";cin>>a;
    cout<<"Digite el valor de B: ";cin>>b;
    result = (a/b) + 1;
    cout.precision(2); //asi puedo redondear a dos decimales - el numero que va () es la cantidad de decimales que redondea
    cout<<"\nEl resultado es: "<<result<<endl;
    return 0;
}