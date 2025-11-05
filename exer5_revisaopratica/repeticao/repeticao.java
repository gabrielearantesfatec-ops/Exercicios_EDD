import java.util.Scanner;

public class repeticao {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Digite um número inteiro");

        if (!sc.hasNextInt()) { System.out.println("Entrada inválida."); return; }
        int a = sc.nextInt();
        System.out.println("\nTabela do " + a + "");
        for (int i = 1; i <= 10; i++) {
            System.out.printf("%d x %d = %d\n", a, i, a * i);
        }

        sc.close();
    }
}

