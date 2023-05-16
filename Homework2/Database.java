

import java.sql.*;

public class Database {

    public static String[] equations;

    public static void main(String[] equations) { 
    

    

    try {
        Database.equations = equations;

        String url = "shu.db";
        String user = "";
        String password = "";

        Connection conn = DriverManager.getConnection(url, user, password);
        Statement stmt = conn.createStatement();
        
        // create the login table if it doesn't exist
        String createTableSQL = "CREATE TABLE IF NOT EXISTS login (username VARCHAR(50), password VARCHAR(50))";
        stmt.executeUpdate(createTableSQL);
        
        // prompt the user to enter their login and password
        System.out.print("Enter your username: ");
        String username = System.console().readLine();
        System.out.print("Enter your password: ");
        String passwordInput = new String(System.console().readPassword());
        
        // query the database for the entered login information
        String selectSQL = "SELECT * FROM login WHERE username = '" + username + "' AND password = '" + passwordInput + "'";
        ResultSet rs = stmt.executeQuery(selectSQL);
        
        // check if the login information is valid
        if (rs.next()) {
            System.out.println("Login successful!");
        } else {
            System.out.println("Incorrect login information.");
        }
        
        conn.close();
    } catch (SQLException ex) {
        System.out.println("SQL Exception: " + ex.getMessage());
    }
    
}
}
