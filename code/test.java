import java.util.*;
import java.io.*;
public class test{
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        Random num = new Random();
        for (int i = 0; i < 32; i++){
            list.add(i);
        }
        Collections.sort(list);
        System.out.println(list);
        System.out.println(sumGrades(list));
        System.out.println(findMedian(list));


      }
    /**
    method that calculates the sum of all values of the list and returns its
    @param list list of all the grades 
    */
      public static double sumGrades(ArrayList<Integer> list){
        double sum = 0;
          for (int i = 0; i < list.size(); i++)
            sum += list.get(i);
        return sum;
      }
    /**
    method that finds the medium of the list of numbers and returns its
    @param list list of all the grades 
    */
      public static double findMedian(ArrayList<Integer> list){
        if (list.size() % 2 == 0){
          int i = list.size() / 2;
          double median = list.get(((i-1)+i)/2);
          return median;
        } else {
          int i = (list.size() / 2) + 1;
          double median = list.get(i);
          return median;
        }
      }
}