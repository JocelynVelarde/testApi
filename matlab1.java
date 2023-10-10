/*
 * Escriba un programa que pida al usuario 10 valores y los agregue a un vector. Debe de pedir un numero positivo, seguido de un negativo,
seguido de un positivo, etc. Hasta llenar las 10 posiciones. Si el usuario no ingresa el valor positivo/negativo esperado, el programa le
permite volver a ingresar el valor hasta que sea correcto. Al finalizar se imprime el vector.
 * 
 * 
 */

import java.util.Scanner;
public class matlab1{
    public static void main(String[] args) {
        int[] vector = new int[10];
        Scanner sc = new Scanner(System.in);
        int i = 0;
        int num = 0;
        while(i < 10){
            System.out.println("Ingrese un numero positivo");
            num = sc.nextInt();
            if(num > 0){
                vector[i] = num;
                i++;
            }
            else{
                System.out.println("Ingrese un numero negativo");
                num = sc.nextInt();
                if(num < 0){
                    vector[i] = num;
                    i++;
                }
            }
        }
    }
}