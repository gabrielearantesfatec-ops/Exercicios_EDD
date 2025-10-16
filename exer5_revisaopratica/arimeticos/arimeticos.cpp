#include <iostream>
using namespace std;

int main() {
    int a, b;
    cout << "Digite dois números inteiros\n";
    if (!(cin >> a >> b)) {
        cerr << "Entrada inválida.\n";
        return 1;
    }

    int soma = a + b, sub = a - b, mul = a * b;
    int resto = (b != 0) ? (a % b) : 0;
    double media = (a + b) / 2.0;

    cout << "\nmultiplicação = " << mul << "\nsubtração = " << sub  << "\nsoma = " << soma  << "\nmédia = " << media << "\nresto = " << resto <<"\n";
    }