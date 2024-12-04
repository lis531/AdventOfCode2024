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
            e.printStackTrace();
        }

        String[] lines = input.toString().split("\n");

        int count = 0;

        for (int i = 0; i < lines.length; i++) {
            for (int j = 0; j < lines[i].length(); j++) {
                if (lines[i].charAt(j) == 'X') {
                    // Horizontal search
                    if (j + 3 < lines[i].length()) {
                        if (lines[i].charAt(j + 1) == 'M' && lines[i].charAt(j + 2) == 'A' && lines[i].charAt(j + 3) == 'S') {
                            count++;
                        }
                    }

                    // Horizontal search backwards
                    if (j - 3 >= 0) {
                        if (lines[i].charAt(j - 1) == 'M' && lines[i].charAt(j - 2) == 'A' && lines[i].charAt(j - 3) == 'S') {
                            count++;
                        }
                    }

                    // Vertical search
                    if (i + 3 < lines.length) {
                        if (lines[i + 1].charAt(j) == 'M' && lines[i + 2].charAt(j) == 'A' && lines[i + 3].charAt(j) == 'S') {
                            count++;
                        }
                    }

                    // Vertical search backwards
                    if (i - 3 >= 0) {
                        if (lines[i - 1].charAt(j) == 'M' && lines[i - 2].charAt(j) == 'A' && lines[i - 3].charAt(j) == 'S') {
                            count++;
                        }
                    }

                    // Diagonal (down-right) search
                    if (i + 3 < lines.length && j + 3 < lines[i].length()) {
                        if (lines[i + 1].charAt(j + 1) == 'M' && lines[i + 2].charAt(j + 2) == 'A' && lines[i + 3].charAt(j + 3) == 'S') {
                            count++;
                        }
                    }

                    // Diagonal (up-left) search
                    if (i - 3 >= 0 && j - 3 >= 0) {
                        if (lines[i - 1].charAt(j - 1) == 'M' && lines[i - 2].charAt(j - 2) == 'A' && lines[i - 3].charAt(j - 3) == 'S') {
                            count++;
                        }
                    }

                    // Diagonal (up-right) search
                    if (i - 3 >= 0 && j + 3 < lines[i].length()) {
                        if (lines[i - 1].charAt(j + 1) == 'M' && lines[i - 2].charAt(j + 2) == 'A' && lines[i - 3].charAt(j + 3) == 'S') {
                            count++;
                        }
                    }

                    // Diagonal (down-left) search
                    if (i + 3 < lines.length && j - 3 >= 0) {
                        if (lines[i + 1].charAt(j - 1) == 'M' && lines[i + 2].charAt(j - 2) == 'A' && lines[i + 3].charAt(j - 3) == 'S') {
                            count++;
                        }
                    }
                }
            }
        }

        System.out.println(count); // Expected output: 18
    }
}
