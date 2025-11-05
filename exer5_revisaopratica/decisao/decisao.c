#include <stdio.h>
int main() {
    int a, b;
    if (scanf("%d %d", &a, &b) != 2) {
        printf("\n\nEntrada inválida.\n");
        return 1;
    }

    printf("Digite dois números inteiros: %d, %d", a, b);
    double media = (a + b) / 2.0;
    if (b == 0) {
        printf("\n\nNota: b é zero -> cuidado com divisão.\n");
    } else if (media >= 10.0) {
        printf("\n\nMédia = %.2f\n", media);
    } else {
        printf("\n\nMédia = %.2f\n", media);
    }



    if (a > 0) {
        if (b > 0) {
            printf("\nAmbos positivos.\n");
        } else {
            printf("\nSomente o primeiro número é positivo.\n");
        }
    } else {
        printf("\nO primeiro número não é positivo.\n");
    }
    


}
    
