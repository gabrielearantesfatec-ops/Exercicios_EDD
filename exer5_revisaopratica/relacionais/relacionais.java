import java.util.Scanner;

public class relacionais {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Digite dois números inteiros \n");

        if (!sc.hasNextInt()) { System.out.println("Entrada inválida."); return; }
        int a = sc.nextInt();
        if (!sc.hasNextInt()) { System.out.println("Entrada inválida."); return; }
        int b = sc.nextInt();

        System.out.println("a > b ? " + (a > b));
        System.out.println("a == b ? " + (a == b));
        System.out.println("Ambos pares? " + (a % 2 == 0 && b % 2 == 0));

        sc.close();
    }
}

