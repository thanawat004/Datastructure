using System;
using System.Data;

class Program
{
    static void Main()
    {
        int[] scores = {10,20,30,40,50,60,70,80,90}; //
    Console.WriteLine("รายการข้อมูลใน Array :");

    //For Loop
    for(int i =0; i <scores.Length; i++)
        {
            Console.WriteLine($"index {i} = {scores[i]}");
        }
        //Foreach
        foreach (int x in scores)
        {
            Console.WriteLine($"Value is : {x}");
        }

        int sum = 0;
        
        for (int i =0; i < scores.Length; i++)
        {
            sum += scores[i];
        }

        //For Max, Min
        int max = scores[0];
        int min = scores[0];

        for (int i =0; i <scores.Length; i++)
        {
            //Max value check
            if(scores[i] > max)
            {
                max = scores[i];
            }

            //Min value check
            if(scores[i] < min)
            {
                min = scores[i];
            }

        }
        Console.WriteLine($"Sum = {sum}");  //ผลรวม
        double avg = (double)sum / scores.Length;
        Console.WriteLine($"Average : {avg}"); //ค่าเฉลี่ย
        Console.WriteLine($"Max = {max}");  //ค่าสูงสุด
        Console.WriteLine($"Min = {min}");  //ค่าต่ำสุด

    }
}
