import java.util.Scanner;

public class decisao {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Digite dois números inteiros\n");

        if (!sc.hasNextInt()) { System.out.println("Entrada inválida."); return; }
        int a = sc.nextInt();
        if (!sc.hasNextInt()) { System.out.println("Entrada inválida."); return; }
        int b = sc.nextInt();

        double media = (a + b) / 2.0;
        System.out.println("Média = "+ a +"");
        if (b == 0) {
            System.out.println("b é zero.");
        } else if (media >= 10.0) {
            System.out.println("Média >= 10.0");
        } else {
            System.out.println("Média < 10.0");
        }

        sc.close();
    }
}

