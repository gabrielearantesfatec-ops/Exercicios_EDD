using System;

class decisao {
    static void Main() {
        Console.Write("Digite dois números inteiros\n");
        string[] parts = Console.ReadLine()?.Split();
        if (parts == null || parts.Length < 2) {
            Console.WriteLine("Entrada inválida.");
            return;
        }

        int a = int.Parse(parts[0]);
        int b = int.Parse(parts[1]);
        double media = (a + b) / 2.0;
        
        Console.WriteLine($"Média = {media}");
        if (b == 0) Console.WriteLine("b é zero (cuidado com divisão).");
        else if (media >= 10.0) Console.WriteLine("Média >= 10.0");
        else Console.WriteLine("Média < 10.0");
    }
}



