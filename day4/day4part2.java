import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        StringBuilder input = new StringBuilder();

        try {
            File myObj = new File("input.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                input.append(myReader.nextLine()).append("\n");
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
        }

        String[] lines = input.toString().split("\n");

        int count = 0;

        for (int i = 0; i < lines.length; i++) {
            for (int j = 0; j < lines[i].length(); j++) {
                boolean right = false;
                boolean left = false;
                if (i - 1 >= 0 && i + 1 < lines.length && j - 1 >= 0 && j + 1 < lines[i].length()) {
                    if (lines[i].charAt(j) == 'A') {
                        if(lines[i - 1].charAt(j - 1) == 'M' && lines[i + 1].charAt(j + 1) == 'S' || lines[i - 1].charAt(j - 1) == 'S' && lines[i + 1].charAt(j + 1) == 'M') {
                            left = true;
                        }
                        if(lines[i + 1].charAt(j - 1) == 'M' && lines[i - 1].charAt(j + 1) == 'S' || lines[i + 1].charAt(j - 1) == 'S' && lines[i - 1].charAt(j + 1) == 'M') {
                            right = true;
                        }
                    }
                }
                if(right && left) {
                    count++;
                }
            }
        }
    System.out.println(count); // Expected output: 9
    }
}
