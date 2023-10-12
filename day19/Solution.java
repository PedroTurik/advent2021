import java.io.FileNotFoundException;

public interface Solution {
    public static void main(String[] args) throws FileNotFoundException {
        var scanners = Parser.parse("input.txt");
        System.out.println(scanners);

    }
}
