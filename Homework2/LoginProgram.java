import java.io.FileWriter;
import java.io.IOException;
import java.sql.DriverManager;
import java.sql.*;

public class LoginProgram {
    public static void main(String[] args) {
        

        try {
            
        FileWriter writer = new FileWriter("shu.db");
            
            for (String equation : Database.equations) {
                writer.write(equation + "\n");
            }
            writer.close();
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
        
        
    }
}