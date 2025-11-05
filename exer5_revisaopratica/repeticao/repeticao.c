#include <stdio.h>

int main() {
    int a, i;
    if (scanf("%d", &a) != 1) {
        printf("Entrada inválida.\n");
        return 1;

    }


    printf("Digite um número inteiro: %d:", a );
    printf("\n\nTabela de %d:\n", a);
    for (i = 1; i <= 10; ++i) {
        printf("%d x %d = %d\n", a, i, a * i);
    }
}
    
