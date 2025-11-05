#include <iostream>
using namespace std;

int main() {
    int a, b;
    cout << "Digite dois valores inteiros: ";
    if (!(cin >> a >> b)) {
        cerr << "\nEntrada inválida.\n";
        return 1;
    }
    
    double media = (a + b) / 2.0;

    if (b == 0) {
        cout << "\nO segundo valor é zero (não dividir!).\n";
    } else {
        cout << "\nMédia = " << media;
        if (media >= 10.0); 
    }

    if (a > 0) {
        if (b > 0) cout << "\nAmbos positivos.\n";
        else cout << "\nSomente o primeiro valor é positivo.\n";
    } else {
        cout << "\n O primeiro valor não é positivo.\n";
    }

    return 0;
}

