package chapter1.samples2;

public class Floats {
    public static void main(String[] args) {
        float f = 100f;

        float test = 0;

        for (int i = 0; i < 1000; i++) {
            test += 1f/10f;
        }

        System.out.println("f = " + f);
        System.out.println("test = " + test);
        System.out.println("equal? " + (f == test));
    }
}