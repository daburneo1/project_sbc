package clases;

public class Reference {

    public int idReference;
    public String title;
    public String date;
    public String doi;

    public Reference() {
    }

    public Reference(int idReference, String title, String date, String doi) {
        this.idReference = idReference;
        this.title = title;
        this.date = date;
        this.doi = doi;
    }

    public int getIdReference() {
        return idReference;
    }

    public void setIdReference(int idReference) {
        this.idReference = idReference;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
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

    @Override
    public String toString() {
        return "Reference{" +
                "idReference=" + idReference +
                ", title='" + title + '\'' +
                ", date='" + date + '\'' +
                ", doi='" + doi + '\'' +
                '}';
    }
}
