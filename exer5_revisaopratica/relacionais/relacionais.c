#include <stdio.h>

int main() {
    int a, b;
    if (scanf("%d %d", &a, &b) != 2) {
        printf("Entrada inválida.\n");
        return 1;
    }
    
    printf("Digite dois números inteiros");
    printf("\n\na > b ? %s\n", (a > b) ? "true" : "false");
    printf("a < b ? %s\n", (a < b) ? "true" : "false");
    printf("a == b ? %s\n", (a == b) ? "true" : "false");
    printf("a != b ? %s\n", (a != b) ? "true" : "false");
    printf("a >= b ? %s\n", (a >= b) ? "true" : "false");
    printf("a <= b ? %s\n", (a <= b) ? "true" : "false");

    
    printf("Ambos pares? %s\n", ( (a % 2 == 0) && (b % 2 == 0) ) ? "true" : "false");

    
    }

    
