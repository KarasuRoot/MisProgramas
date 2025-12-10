/* Escriba la siguiente expresion matematica como expresion en C++
a+b/c+d (a más b sobre c más d)
*/
//Asi lo resolvi yo - y Alejandro tambien (Verificado)
#include<iostream>
using namespace std;
int main(){
    float a,b,c,d,resul=0;
    cout<<"Digite el valor de A: ";cin>>a;
    cout<<"Digite el valor de B: ";cin>>b;
    cout<<"Digite el valor de C: ";cin>>c;
    cout<<"Digite el valor de D: ";cin>>d;
    resul = (a+b) / (c+d);
    cout.precision(2);
    cout<<"\nEl resultado es: "<<resul<<endl;


    return 0;
}


