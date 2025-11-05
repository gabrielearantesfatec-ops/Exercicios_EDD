using System;

class aritmeticos {
    static void Main() {
        Console.Write("Digite dois números inteiros");
        string[] parts = Console.ReadLine()?.Split();
        if (parts == null || parts.Length < 2) {
            Console.WriteLine("Entrada inválida.");
            return;
        }

        int a = int.Parse(parts[0]);
        int b = int.Parse(parts[1]);

        int soma = a + b;
        int sub = a - b;
        int mul = a * b;
        int div_int = (b != 0) ? (a / b) : 0;
        double div_real = (b != 0) ? (double)a / b : 0.0;
        int resto = (b != 0) ? (a % b) : 0;
        double media = (a + b) / 2.0;

        Console.WriteLine($"\nsoma = {soma}\nsub = {sub}\nmul = {mul}\ndiv int = {div_int}\ndiv real = {div_real:F4}\nresto = {resto}\nmedia = {media:F2}");
    }
}

