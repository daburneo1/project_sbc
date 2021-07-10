package data;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DATConexion {
    public static Connection con;

    public static Connection getConnection() throws SQLException, ClassNotFoundException{
        String driver = "com.mysql.cj.jdbc.Driver";
        String url = "jdbc:mysql://localhost/covid19_semantic?useSSL=false";
        Class.forName(driver);
        return DriverManager.getConnection(url, "root", "");
    }

    public Connection AbrirConexion() throws ClassNotFoundException, SQLException {
        con = getConnection();
        return con;
    }

    public void CerrarConexion() throws SQLException {
        con.close();
    }
}
