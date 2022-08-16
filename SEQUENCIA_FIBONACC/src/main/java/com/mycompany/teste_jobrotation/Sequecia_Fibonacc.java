
package com.mycompany.teste_jobrotation;

import static java.sql.DriverManager.println;
import java.util.Scanner;
/**
 sequecia de Fibonacc
 */
public class Sequecia_Fibonacc {

    public static void main(String[] args) {
        Scanner ler= new Scanner(System.in);
        int num ,t1=0, t2=1,t3=0;
	
         
            System.out.println("Digite um numero:\n");
              num=ler.nextInt();
		
	while (num > t3){
		t3=t1+t2;
		t1=t2;
		t2=t3;
		}
        if( num == 0 || num == 1){
			 
            System.out.println("Este numero pertence a sequencia de Fibonacc ");
		 	
	}
	else if( num == t3){
           System.out.println("Este numero pertence a sequencia de Fibonacc ");
			 
	}
	else {
            System.out.println("Este numero nao pertence a sequencia de Fibonacc ");
			 
	}
    }

   
}
