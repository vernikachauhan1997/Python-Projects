import java.util.*;
class TestClass {
    public static void main(String args[] ) throws Exception {
            try {
                 Scanner sc = new Scanner(System.in);
                int t = sc.nextInt();
                while (t -->0)
                {
                    int n = sc.nextInt();
                    String str = sc.next();
                long c = 0;
                    for(int i = 0; i<n; i++){
                        if(str.charAt(i) == '1')
                            c++;
                    }
                    System.out.println(c*(c+1)/2);
                }
            }catch(Exception e){
                return;
            }
    }
}
