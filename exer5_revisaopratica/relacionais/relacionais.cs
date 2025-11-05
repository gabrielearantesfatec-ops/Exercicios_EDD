using System;

class relacionais {
    static void Main() {
        Console.Write("Digite dois números inteiros\n");
        string[] parts = Console.ReadLine()?.Split();
        if (parts == null || parts.Length < 2) {
            Console.WriteLine("Entrada inválida.");
            return;
        }

        int a = int.Parse(parts[0]);
        int b = int.Parse(parts[1]);

        Console.WriteLine($"a > b ? { (a > b) }");
        Console.WriteLine($"a = b ? { (a == b) }");
        Console.WriteLine($"Ambos pares? { (a % 2 == 0 && b % 2 == 0) }");
    }
}


