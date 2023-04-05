import java.io.FileWriter;
import java.io.IOException;


public class LoginProgram {
    public static void main(String[] args) {
        Database.equations = new String[] {
            "SELECT * FROM login WHERE username = 'username' AND password = 'password'",
        }
;

        try {
            FileWriter writer = new FileWriter("shu.sql");
            
            for (String equation : Database.equations) {
                writer.write(equation + "\n");
            }
            writer.close();
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
        
        
    }
}