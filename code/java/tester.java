import java.util.Scanner;
public class tester {
    public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      int ROWS = sc.nextInt();
      int COLS = sc.nextInt();
      int [][] values = new int [ROWS][COLS];
      for( int i = 0; i < values.length; i++ ) {
        for( int j = 0; j < values[0].length; j++ ) {
            values[i][j] = 0;
        }
      }
      for( int i = 0; i < values.length; i++ ) {
        for( int j = 0; j < values[0].length; j++ ) {
          System.out.print( values[i][j] );
        }
      System.out.println();
      }
      
    }
  
}
