package clases;

import java.util.ArrayList;

public class Article {
    public int idArticle;
    public String abstractText;
    public String title;
    public String uri;
    public String date;
    public String doi;
    public String identifier;
    public String language;
    public String isAccesible;
    public int numCiting;
    public String venue;
    public ArrayList<Author> ArrayAuthors;
    public ArrayList<FieldStudy> ArrayFieldStudy;
    public ArrayList<Reference> ArrayReferences;

    public Article() {
    }

    public Article(int idArticle, String abstractText, String title, String uri, String date, String doi, String identifier, String language, String isAccesible, int numCiting, String venue, ArrayList<Author> arrayAuthors, ArrayList<FieldStudy> arrayFieldStudy, ArrayList<Reference> arrayReferences) {
        this.idArticle = idArticle;
        this.abstractText = abstractText;
        this.title = title;
        this.uri = uri;
        this.date = date;
        this.doi = doi;
        this.identifier = identifier;
        this.language = language;
        this.isAccesible = isAccesible;
        this.numCiting = numCiting;
        this.venue = venue;
        ArrayAuthors = arrayAuthors;
        ArrayFieldStudy = arrayFieldStudy;
        ArrayReferences = arrayReferences;
    }

    public int getIdArticle() {
        return idArticle;
    }

    public void setIdArticle(int idArticle) {
        this.idArticle = idArticle;
    }

    public String getVenue() {
        return venue;
    }

    public void setVenue(String venue) {
        this.venue = venue;
    }

    public int getNumCiting() {
        return numCiting;
    }

    public void setNumCiting(int numCiting) {
        this.numCiting = numCiting;
    }

    public String getAbstractText() {
        return abstractText;
    }

    public void setAbstractText(String abstractText) {
        this.abstractText = abstractText;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public String getDoi() {
        return doi;
    }

    public void setDoi(String doi) {
        this.doi = doi;
    }

    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }

    public String getIsAccesible() {
        return isAccesible;
    }

    public void setIsAccesible(String isAccesible) {
        this.isAccesible = isAccesible;
    }

    public ArrayList<Author> getArrayAuthors() {
        return ArrayAuthors;
    }

    public void setArrayAuthors(ArrayList<Author> arrayAuthors) {
        ArrayAuthors = arrayAuthors;
    }

    public ArrayList<FieldStudy> getArrayFieldStudy() {
        return ArrayFieldStudy;
    }

    public void setArrayFieldStudy(ArrayList<FieldStudy> arrayFieldStudy) {
        ArrayFieldStudy = arrayFieldStudy;
    }

    public ArrayList<Reference> getArrayReferences() {
        return ArrayReferences;
    }

    public void setArrayReferences(ArrayList<Reference> arrayReferences) {
        ArrayReferences = arrayReferences;
    }

    @Override
    public String toString() {
        return "Article{" +
                "idArticle=" + idArticle +
                ", abstractText='" + abstractText + '\'' +
                ", title='" + title + '\'' +
                ", uri='" + uri + '\'' +
                ", date='" + date + '\'' +
                ", doi='" + doi + '\'' +
                ", identifier='" + identifier + '\'' +
                ", language='" + language + '\'' +
                ", isAccesible='" + isAccesible + '\'' +
                ", numCiting=" + numCiting +
                ", venue='" + venue + '\'' +
                ", ArrayAuthors=" + ArrayAuthors +
                ", ArrayFieldStudy=" + ArrayFieldStudy +
                ", ArrayReferences=" + ArrayReferences +
                '}';
    }
}
