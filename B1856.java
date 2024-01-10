// Problem- https://codeforces.com/contest/1896/problem/B
import java.util.*;
public class B1856{
    public static void main(String []arg){
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0) {
            int length=sc.nextInt();
            String s=sc.next();
            int A=0,count=0;
            for(int i=0;i<length;i++){
                if(s.charAt(i)=='A')
                    A++;
                else{
                    count+=(count>0 ?1:0);
                    count+=A;
                    A=0;
                }
            }
            System.out.println(count);
        }
    }
}
