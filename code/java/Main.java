import java.util.Random;
import java.util.Scanner;
public class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int row = sc.nextInt();
    int cols = sc.nextInt();
    int mines = 5;
    int [][] values = new int [row][cols];
    for( int i = 0; i < values.length; i++ ) {
      for( int j = 0; j < values[0].length; j++ ) {
          values[i][j] = 0;
      }
    }
    placeMines(values, 5);
    fill(values);
    for( int i = 0; i < values.length; i++ ) {
      for( int j = 0; j < values[0].length; j++ ) {
        System.out.print( values[i][j] );
      }
    System.out.println();
    }

  }
  public static void placeMines(int[][] grid, int mines){
    for(int i = 0; i < mines; i++){
      Random rand = new Random();
      int j = rand.nextInt(grid.length);
      int k = rand.nextInt(grid[0].length);
      if (grid[j][k] != 9){
        grid[j][k] = 9;
      }
    }
  }
  
  public static void fill(int[][] grid) {
    for(int i = 0; i < grid.length; i++){
      for(int j = 0; j < grid[0].length; j++){
        int count = 0;
        if(grid[i][j] != 9){
          if(i == 0){
            for(int k = 0; k < 9; k++){
          
          
            count++;
            }
         }
         grid[i][j] = count;
        }
      }
    }
  }

  
}