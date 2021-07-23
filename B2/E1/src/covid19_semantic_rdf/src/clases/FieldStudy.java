package clases;

public class FieldStudy {
    public int idFieldStudy;
    public String FieldStudy;

    public FieldStudy() {
    }

    public FieldStudy(int idFieldStudy, String fieldStudy) {
        this. idFieldStudy = idFieldStudy;
        this. FieldStudy = fieldStudy;
    }

    public int getIdFieldStudy() {
        return idFieldStudy;
    }

    public void setIdFieldStudy(int idFieldStudy) {
        this.idFieldStudy = idFieldStudy;
    }

    public String getFieldStudy() {
        return FieldStudy;
    }

    public void setFieldStudy(String fieldStudy) {
        FieldStudy = fieldStudy;
    }

    @Override
    public String toString() {
        return "FieldStudy{" +
                "idFieldStudy=" + idFieldStudy +
                ", FieldStudy='" + FieldStudy + '\'' +
                '}';
    }
}
