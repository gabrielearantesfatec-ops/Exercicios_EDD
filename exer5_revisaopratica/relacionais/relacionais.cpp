#include <iostream>
using namespace std;

int main() {
    int a, b;
    cout << "Digite dois valores inteiros";
    if (!(cin >> a >> b)) {
        cerr << "Entrada inválida.\n";
        return 1;
    }

    cout << boolalpha;
    cout << "\n\na > b ? " << (a > b) << "\na < b ? " << (a < b)
         << "\na == b ? " << (a == b) << "\na != b ? " << (a != b) << "\n";
    cout << "\nAmbos pares? " << ((a % 2 == 0) && (b % 2 == 0)) << "\n";

    
}