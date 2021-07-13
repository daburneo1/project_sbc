package logic;

import clases.Article;
import clases.Author;
import clases.FieldStudy;
import clases.Reference;
import com.cybozu.labs.langdetect.Detector;
import com.cybozu.labs.langdetect.DetectorFactory;
import com.cybozu.labs.langdetect.LangDetectException;

import data.DATExtract;

import java.io.IOException;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.util.ArrayList;

public class build {

    DATExtract DATA = new DATExtract();
    Detector d;

    public Article BuildArticle(int id) throws SQLException, ClassNotFoundException, IOException, LangDetectException {
        Article objArticle = new Article();
        ArrayList<Author> ArrayAuthors = new ArrayList<Author>();
        ArrayList<FieldStudy> ArrayFieldsStudy = new ArrayList<FieldStudy>();
        ArrayList<Reference> ArrayReferences = new ArrayList<Reference>();

        objArticle = FindArticle(id);
        ArrayAuthors = FindAuthors(objArticle);
        ArrayFieldsStudy = FindFieldsStudy(objArticle);
        ArrayReferences = FindReferences(objArticle);

        objArticle.setArrayAuthors(ArrayAuthors);
        objArticle.setArrayFieldStudy(ArrayFieldsStudy);
        objArticle.setArrayReferences(ArrayReferences);

        return objArticle;
    }

    private ArrayList<Reference> FindReferences(Article objArticle) throws SQLException, ClassNotFoundException {
        ArrayList<Reference> ArrayReferences = new ArrayList<Reference>();
        ResultSet rs;
        rs = DATA.FindReferences(objArticle);
        ResultSetMetaData rm = rs.getMetaData();

        int columnCount = rm.getColumnCount();
        ArrayList<String> columns = new ArrayList<>();
        for (int i = 1; i <= columnCount; i++){
            String columnName = rm.getColumnName(i);
            columns.add(columnName);
        }
        while(rs.next()){
            Reference objReference = new Reference();
            for(String columnName : columns){
                String value = rs.getString(columnName);
                if(columnName.equals("idReference")){
                    objReference.setIdReference(Integer.parseInt(value));
                }
                if(columnName.equals("doi")){
                    objReference.setDoi(value);
                }
                if(columnName.equals("title")){
                    objReference.setTitle(value);
                }
                if(columnName.equals("year")){
                    objReference.setDate(value);
                }
            }
            ArrayReferences.add(objReference);
        }
        DATA.CerrarConexion();
        return ArrayReferences;
    }

    private ArrayList<FieldStudy> FindFieldsStudy(Article objArticle) throws SQLException, ClassNotFoundException {
        ArrayList<FieldStudy> ArrayFieldsStudy = new ArrayList<FieldStudy>();
        ResultSet rs;
        rs = DATA.FindFieldsStudy(objArticle);
        ResultSetMetaData rm = rs.getMetaData();

        int columnCount = rm.getColumnCount();
        ArrayList<String> columns = new ArrayList<>();
        for (int i = 1; i <= columnCount; i++){
            String columnName = rm.getColumnName(i);
            columns.add(columnName);
        }
        while(rs.next()){
            FieldStudy objFieldStudy = new FieldStudy();
            for(String columnName : columns){
                String value = rs.getString(columnName);
                if(columnName.equals("idfieldStudy")){
                    objFieldStudy.setIdFieldStudy(Integer.parseInt(value));
                }
                if(columnName.equals("fieldStudy")){
                    objFieldStudy.setFieldStudy(value);
                }
            }
            ArrayFieldsStudy.add(objFieldStudy);
        }
        DATA.CerrarConexion();
        return ArrayFieldsStudy;
    }

    private ArrayList<Author> FindAuthors(Article objArticle) throws SQLException, ClassNotFoundException {
        ArrayList<Author> ArrayAuthors = new ArrayList<Author>();
        ResultSet rs;
        rs = DATA.FindAuthors(objArticle);
        ResultSetMetaData rm = rs.getMetaData();

        int columnCount = rm.getColumnCount();
        ArrayList<String> columns = new ArrayList<>();
        for (int i = 1; i <= columnCount; i++){
            String columnName = rm.getColumnName(i);
            columns.add(columnName);
        }
        while(rs.next()){
            Author objAuthor = new Author();
            for(String columnName : columns){
                String value = rs.getString(columnName);
                if(columnName.equals("idAuthor")){
                    objAuthor.setIdAuthor(Integer.parseInt(value));
                }
                if(columnName.equals("name")){
                    objAuthor.setName(value);
                }
                if(columnName.equals("url")){
                    objAuthor.setUrl(value);
                }
                if(columnName.equals("influentialCitationCount")){
                    objAuthor.setInfluentialCC(Integer.parseInt(value));
                }
                if(columnName.equals("id")){
                    objAuthor.setId(value);
                }
            }
            ArrayAuthors.add(objAuthor);
        }
        DATA.CerrarConexion();
        return ArrayAuthors;
    }

    public Article FindArticle (int id) throws SQLException, ClassNotFoundException, IOException, LangDetectException {
        ResultSet rs;
        rs = DATA.FindArticle(id);
        ResultSetMetaData rm = rs.getMetaData();
        int columnCount = rm.getColumnCount();
        ArrayList<String> columns = new ArrayList<>();
        for (int i = 1; i <= columnCount; i++){
            String columnName = rm.getColumnName(i);
            columns.add(columnName);
        }

        Article a = new Article();
        while(rs.next()){
            for (String columnName : columns){
                String value = rs.getString(columnName);
                if(columnName.equals("journalArticleId")){
                    a.setIdArticle(Integer.parseInt(value));
                }
                if(columnName.equals("abstract")){
                    a.setAbstractText(value);
                }
                if(columnName.equals("doi")){
                    a.setDoi(value);
                }
                if(columnName.equals("isOpenAccess")){
                    if (Integer.parseInt(value) == 1){
                        a.setIsAccesible("true");
                    }else if (Integer.parseInt(value) == 0){
                        a.setIsAccesible("false");
                    }
                }
                if(columnName.equals("numCiting")){
                    a.setNumCiting(Integer.parseInt(value));
                }
                if(columnName.equals("paperId")){
                    a.setIdentifier(value);
                }
//                if(columnName.equals("title")){
//                    a.setTitle(value);
//                    String language = detectLanguage(value);
//                    a.setLanguage(language);
//                }
                if(columnName.equals("venue")){
                    a.setVenue(value);
                }
                if(columnName.equals("url")){
                    a.setUri(value);
                }
                if(columnName.equals("year")){
                    a.setDate(value);
                }
            }
        }
        DATA.CerrarConexion();
        return a;
    }

    public String detectLanguage(String value) throws IOException, LangDetectException {
        //String profileDirectory = "C:\\Program Files\\Java\\jdk-12\\lib\\langdetect-09-13-2011\\profiles";
        try{
            //DetectorFactory.loadProfile(profileDirectory);
            //Detector d = DetectorFactory.create();
            d.append(value);
            return d.detect();
        } catch (LangDetectException e) {
            e.printStackTrace();
        }
        return null;

    }


//    public void CreateDetectorFactory() throws LangDetectException {
//        DetectorFactory.loadProfile("C:\\Program Files\\Java\\jdk-12\\lib\\langdetect-09-13-2011\\profiles");
//        {
//            try {
//                d = DetectorFactory.create();
//            } catch (LangDetectException e) {
//                e.printStackTrace();
//            }
//        }
//    }
}
