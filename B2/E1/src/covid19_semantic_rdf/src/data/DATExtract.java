package data;

import clases.Article;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class DATExtract {

    DATConexion c = new DATConexion();

    public ResultSet FindArticle(int id) throws SQLException, ClassNotFoundException {
        Statement st = c.AbrirConexion().createStatement();
        String sentencia = "SELECT * FROM Journal_Article WHERE journalArticleId = " + id + ";";
        ResultSet rs = st.executeQuery(sentencia);
        return rs;
    }

    public ResultSet FindAuthors(Article objArticle) throws SQLException, ClassNotFoundException {
        Statement st = c.AbrirConexion().createStatement();
        String sentencia = "SELECT * FROM Author WHERE JournalArticleId = " + objArticle.getIdArticle() + ";";
        ResultSet rs = st.executeQuery(sentencia);
        return rs;
    }

    public ResultSet FindFieldsStudy(Article objArticle) throws SQLException, ClassNotFoundException {
        Statement st = c.AbrirConexion().createStatement();
        String sentencia = "SELECT * FROM Field_Study WHERE JournalArticleId = " + objArticle.getIdArticle() + ";";
        ResultSet rs = st.executeQuery(sentencia);
        return rs;
    }

    public ResultSet FindReferences(Article objArticle) throws SQLException, ClassNotFoundException {
        Statement st = c.AbrirConexion().createStatement();
        String sentencia = "SELECT * FROM Reference WHERE JournalArticleId = " + objArticle.getIdArticle() + ";";
        ResultSet rs = st.executeQuery(sentencia);
        return rs;
    }

    public void CerrarConexion() throws SQLException {
        c.CerrarConexion();
    }
}
