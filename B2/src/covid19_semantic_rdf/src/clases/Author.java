package clases;

public class Author {

    public int idAuthor;
    public String name;
    public String url;
    public int influentialCC;
    public String id;

    public Author() {
    }

    public Author(int idAuthor, String name, String url, int influentialCC, String id) {
        this.idAuthor = idAuthor;
        this.name = name;
        this.url = url;
        this.influentialCC = influentialCC;
        this.id = id;
    }

    public int getIdAuthor() {
        return idAuthor;
    }

    public void setIdAuthor(int idAuthor) {
        this.idAuthor = idAuthor;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public int getInfluentialCC() {
        return influentialCC;
    }

    public void setInfluentialCC(int influentialCC) {
        this.influentialCC = influentialCC;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    @Override
    public String toString() {
        return "Author{" +
                "idAuthor=" + idAuthor +
                ", name='" + name + '\'' +
                ", url='" + url + '\'' +
                ", influentialCC=" + influentialCC +
                ", id='" + id + '\'' +
                '}';
    }
}
