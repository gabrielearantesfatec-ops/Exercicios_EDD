using System;

class repeticoes {
    static void Main() {
        Console.Write("Digite dois inteiros: ");
        string[] parts = Console.ReadLine()?.Split();
        if (parts == null || parts.Length < 2) {
            Console.WriteLine("Entrada inválida.");
            return;
        }

        int a = int.Parse(parts[0]);
        int b = int.Parse(parts[1]);

        Console.WriteLine($"\nTabela do {a}");
        for (int i = 1; i <= 10; i++)
            Console.WriteLine($"{a} x {i} = {a * i}");
    }
}



