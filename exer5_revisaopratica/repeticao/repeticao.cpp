#include <iostream>
using namespace std;

int main() {
    int a;
    cout << "Digite um número inteiro\n";
    if (!(cin >> a)) {
        cerr << "Entrada inválida.\n\n";
        return 1;
    }
    cout << "\nTabela do " << a << "\n";
    for (int i = 1; i <= 10; ++i) cout << a << " x " << i << " = " << a * i << "\n";
}
