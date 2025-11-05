import java.util.Scanner;

public class aritmeticos {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Digite dois números inteiros");

        if (!sc.hasNextInt()) { System.out.println("Entrada inválida."); return; }
        int a = sc.nextInt();
        if (!sc.hasNextInt()) { System.out.println("Entrada inválida."); return; }
        int b = sc.nextInt();

        int soma = a + b;
        int sub = a - b;
        int mul = a * b;
        int div_int = (b != 0) ? (a / b) : 0;
        double div_real = (b != 0) ? (double)a / b : 0.0;
        int resto = (b != 0) ? a % b : 0;
        double media = (a + b) / 2.0;

        System.out.printf("\nsoma = %d\nsub = %d\nmul = %d\ndiv int = %d\ndiv real = %.4f\nresto = %d\nmedia = %.2f\n",
                          soma, sub, mul, div_int, div_real, resto, media);

        sc.close();
    }
}
