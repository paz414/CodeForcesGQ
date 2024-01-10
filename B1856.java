import java.util.*;
public class B1856{
    public static void main(String []arg){
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0) {
           int length=sc.nextInt();
           String s=sc.next();
           int x=s.indexOf('A'),y=s.lastIndexOf('B');
           if((x>y) || (s.indexOf('B')==-1) || (s.indexOf('A')==-1))
               System.out.println(0);
           else
               System.out.println(y-x);


        }
    }
}
