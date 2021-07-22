package logic;

import java.io.*;
import java.sql.SQLException;

import clases.Article;
import com.cybozu.labs.langdetect.LangDetectException;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.ModelFactory;
import org.apache.jena.rdf.model.Property;
import org.apache.jena.rdf.model.Resource;
import org.apache.jena.rdf.model.ResourceFactory;
import org.apache.jena.riot.Lang;
import org.apache.jena.riot.RDFDataMgr;
import org.apache.jena.vocabulary.RDF;

public class main {
    public static void main(String[] args) throws IOException, SQLException, ClassNotFoundException, LangDetectException {

        Article objArticle = new Article();
        build build = new build();


        Model model = ModelFactory.createDefaultModel();
        Model extModel = ModelFactory.createDefaultModel();
        // Prefix
        String dataPrefix = "http://utpl.edu.ec/sbc/";
        model.setNsPrefix("journalArticle", dataPrefix);

        String projmolPrefix = "http://example.org/projmol";
        model.setNsPrefix("projmol", projmolPrefix);

        String c4oPrefix = "http://purl.org/spar/c4o/";
        model.setNsPrefix("c4o", c4oPrefix);

        String dboPrefix = "http://dbpedia.org/ontology";
        model.setNsPrefix("dbo", dboPrefix);

        String vivoPrefix = "http://vivoweb.org/ontology/core#";
        model.setNsPrefix("vivo", vivoPrefix);

        String biboPrefix = "http://purl.org/ontology/bibo/";
        model.setNsPrefix("bibo", biboPrefix);

        String foafPrefix = "http://xmlns.com/foaf/0.1/";
        model.setNsPrefix("foaf", foafPrefix);

        String dcePrefix = "http://purl.org/dc/elements/1.1/";
        model.setNsPrefix("dce", dcePrefix);

        String dctPrefix = "http://purl.org/dc/terms/";
        model.setNsPrefix("dct", dctPrefix);

        String skosPrefix = "http://www.w3.org/2004/02/skos/core#/";
        model.setNsPrefix("skos", skosPrefix);

        String schemaPrefix = "http://schema.org/";
        model.setNsPrefix("schema", schemaPrefix);

        // Classes
        String articleClassURI = vivoPrefix + "Article";
        Resource Article = extModel.getResource(articleClassURI);

        String personClassURI = foafPrefix + "Person";
        Resource Person = extModel.getResource(personClassURI);

        String GlobalCitationCountClassURI = c4oPrefix + "GlobalCitationCount";
        Resource GlobalCitationCount = extModel.getResource(GlobalCitationCountClassURI);

        String ConcepClassURI = skosPrefix + "Concept";
        Resource Concept = extModel.getResource(ConcepClassURI);

        String JournalClassURI = biboPrefix + "Journal";
        Resource Journal = extModel.getResource(JournalClassURI);

        String abstractPropURI = biboPrefix + "abstract";
        Property abstractProperty = ResourceFactory.createProperty(abstractPropURI);

        String titlePropURI = dctPrefix + "title";
        Property titleProperty = ResourceFactory.createProperty(titlePropURI);

        String uriPropURI = biboPrefix + "uri";
        Property uriProperty = ResourceFactory.createProperty(uriPropURI);

        String datePropURI = dctPrefix + "date";
        Property dateProperty = ResourceFactory.createProperty(datePropURI);

        String doiPropURI = biboPrefix + "doi";
        Property doiProperty = ResourceFactory.createProperty(doiPropURI);

        String identifierPropURI = vivoPrefix + "identifier";
        Property identifierProperty = ResourceFactory.createProperty(identifierPropURI);

        String languagePropURI = dcePrefix + "language";
        Property languageProperty = ResourceFactory.createProperty(languagePropURI);

        String accessiblePropURI = schemaPrefix + "isAccessibleForFree";
        Property accessibleProperty = ResourceFactory.createProperty(accessiblePropURI);

        String citesPropURI = biboPrefix + "cites";
        Property citesProperty = ResourceFactory.createProperty(citesPropURI);

        String isPartOfPropURI = dboPrefix + "isPartOf";
        Property isPartOfProperty = ResourceFactory.createProperty(isPartOfPropURI);

        String namePropURI = foafPrefix + "name";
        Property nameProperty = ResourceFactory.createProperty(namePropURI);

        String subjectPropURI = dctPrefix + "subject";
        Property subjectProperty = ResourceFactory.createProperty(subjectPropURI);

        String hasGlobalCountDatePropURI = c4oPrefix + "hasGlobalCountDate";
        Property hasGlobalCountDateProperty = ResourceFactory.createProperty(hasGlobalCountDatePropURI);

        String hasGlobalCountValuePropURI = c4oPrefix + "hasGlobalCountValue";
        Property hasGlobalCountValueProperty = ResourceFactory.createProperty(hasGlobalCountValuePropURI);

        String creatorPropURI = dctPrefix + "creator";
        Property creatorProperty = ResourceFactory.createProperty(creatorPropURI);

        String rankPropURI = vivoPrefix + "rank";
        Property rankProperty = ResourceFactory.createProperty(rankPropURI);

        String influentialCCPropURI = projmolPrefix + "influentialCC";
        Property influentialProperty = ResourceFactory.createProperty(influentialCCPropURI);

        String prefLabelPropURI = skosPrefix + "prefLabel";
        Property prefLabelProperty = ResourceFactory.createProperty(prefLabelPropURI);

        Resource article = null;

//        build.CreateDetectorFactory();

        for (int i = 1; i <=1496; i++) {
            System.out.println(i);
            objArticle = build.BuildArticle(i);
            System.out.println(objArticle.toString());
            String articleURI = dataPrefix + objArticle.getIdentifier();

            article = model.createResource(articleURI)
                    .addProperty(RDF.type, Article);

            if (objArticle.getAbstractText() != null) {
                article.addProperty(abstractProperty, objArticle.getAbstractText());
            }
            if (objArticle.getTitle() != null) {
                article.addProperty(titleProperty, objArticle.getTitle());
            }
            if (objArticle.getUri() != null) {
                Resource uri = model.createResource(objArticle.getUri());
                article.addProperty(uriProperty, uri);
            }
            if (objArticle.getDate() != null) {
                article.addProperty(dateProperty, objArticle.getDate());
            }
            if (objArticle.getDoi() != null) {
                article.addProperty(doiProperty, objArticle.getDoi());
            }
            if (objArticle.getIdentifier() != null) {
                article.addProperty(identifierProperty, objArticle.getIdentifier());
            }
            if (objArticle.getLanguage() != null) {
                article.addProperty(languageProperty, objArticle.getLanguage());
            }
            if (objArticle.getIsAccesible() != null) {
                article.addProperty(accessibleProperty, objArticle.getIsAccesible());
            }
            if (objArticle.getArrayReferences() != null) {
                for (int j = 0; j < objArticle.getArrayReferences().size(); j++) {
                    String referenceURI = dataPrefix + objArticle.getArrayReferences().get(j).getDoi()
                            .replace(" ", "_")
                            .replace("/", "")
                            .replace("(", "")
                            .replace(")", "")
                            .replace("%","")
                            .replace(".", "")
                            .replace("<", "")
                            .replace(">", "");
                    Resource reference = model.createResource(referenceURI);
                    article.addProperty(citesProperty, reference);
                    model.createResource(referenceURI)
                            .addProperty(RDF.type, Article)
                            .addProperty(titleProperty, objArticle.getArrayReferences().get(j).getTitle())
                            .addProperty(dateProperty, objArticle.getArrayReferences().get(j).getDate())
                            .addProperty(doiProperty, objArticle.getArrayReferences().get(j).getDoi());
                }
                String CitationFrecuencyURI = dataPrefix + "g-citation-" + objArticle.getIdentifier() + "-2021-05-06";
                Resource hasGlobalCountDate = model.createResource(CitationFrecuencyURI);
                article.addProperty(hasGlobalCountDateProperty, hasGlobalCountDate);
                model.createResource(CitationFrecuencyURI)
                        .addProperty(RDF.type, GlobalCitationCount)
                        .addProperty(hasGlobalCountDateProperty, "'2021-05-16'^^xsd:date")
                        .addProperty(hasGlobalCountValueProperty, "'" + String.valueOf(objArticle.getArrayReferences().size()) + "'" + "^^xsd:nonNegativeInteger");
            }
            if (objArticle.getArrayFieldStudy() != null) {
                for (int j = 0; j < objArticle.getArrayFieldStudy().size(); j++) {
                    String topicsURI = dataPrefix + objArticle.getArrayFieldStudy().get(j).getFieldStudy().replace(" ", "_");
                    Resource subject = model.createResource(topicsURI);
                    article.addProperty(subjectProperty, subject);
                    model.createResource(topicsURI)
                            .addProperty(RDF.type, Concept)
                            .addProperty(prefLabelProperty, objArticle.getArrayFieldStudy().get(j).getFieldStudy());
                }
            }
            if (!objArticle.getVenue().equals("")) {
                String journalURI = dataPrefix + objArticle.getVenue().replace(" ", "_")
                        .replace(".", "");
                Resource venue = model.createResource(journalURI);
                article.addProperty(isPartOfProperty, venue);
                model.createResource(journalURI)
                        .addProperty(RDF.type, Journal)
                        .addProperty(nameProperty, objArticle.getVenue());
            }
            if (objArticle.getArrayAuthors() != null) {
                for (int j = 0; j < objArticle.getArrayAuthors().size(); j++) {
                    String creatorURI = dataPrefix + objArticle.getArrayAuthors().get(j).getName().replace(" ", "_")
                            .replace("Ñ", "N")
                            .replace("ñ", "n")
                            .replace(".", "");
                    Resource creator = model.createResource(creatorURI);
                    article.addProperty(creatorProperty, creator);
                    Resource uriAuthor = model.createResource(objArticle.getArrayAuthors().get(j).getUrl());
                    model.createResource(creatorURI)
                            .addProperty(RDF.type, Person)
                            .addProperty(nameProperty, objArticle.getArrayAuthors().get(j).getName())
                            .addProperty(uriProperty, uriAuthor)
                            .addProperty(influentialProperty, String.valueOf(objArticle.getArrayAuthors().get(j).getInfluentialCC()))
                            .addProperty(rankProperty, String.valueOf(j + 1));
                }
            }
        }

        model.add(article, RDF.type, Article);

        File f = new File("C:\\Users\\Davicho\\OneDrive - Universidad Técnica Particular de Loja - UTPL\\Documentos\\Sistemas\\10mo\\SBC\\Repositorio\\project_sbc\\B2\\src\\covid19_semantic_rdf\\data\\covid19_semantic.rdf");
        FileOutputStream os = new FileOutputStream(f);

        model.write(System.out, "N3"); //xml
        RDFDataMgr.write(os, model, Lang.RDFXML);

        model.close();

    }
}
