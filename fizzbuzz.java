

public class fizzbuzz {
    public static void main(String[] args){
        for(int i = 0; i<=100; i++){
            if(i%3 == 0 && i%5==0){
                System.out.println("fizzbuzz with: " +i);
                continue;
            }
            if(i%3 == 0){
                System.out.println("fizz with: " +i);
            }
            if(i%5 == 0){
                System.out.println("buzz with: " +i);
            }
        }
    }
}
