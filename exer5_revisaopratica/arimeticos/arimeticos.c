#include <stdio.h>

int main() {
    int a, b;
    
    if (scanf("%d %d", &a, &b) != 2) {
        printf("Entrada inválida.\n");
        return 1;
    }
    
    printf("Digite dois números inteiros: %d, %d", b, a);
    int soma = a + b;
    int sub = a - b;
    int mul = a * b;
    int div_int = (b != 0) ? (a / b) : 0; // evitar divisão por zero
    double div_real = (b != 0) ? ((double)a / (double)b) : 0.0;
    int resto = (b != 0) ? (a % b) : 0;
    double media = (a + b) / 2.0;

    printf("\n\nsoma = %d\nsub = %d\nmul = %d\ndiv int = %d\ndiv real = %.4f\nresto = %d\nmedia = %.2f\n",
           soma, sub, mul, div_int, div_real, resto, media);

}
    
