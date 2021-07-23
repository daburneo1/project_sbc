from SPARQLWrapper import SPARQLWrapper, JSON


def loadData():
    sparql = SPARQLWrapper("http://localhost:7200/repositories/covid19_sbc")
    sparql.setQuery("""
        PREFIX dct: <http://purl.org/dc/terms/>

        select ?article where { 
	    ?s dct:title ?article .
        } LIMIT 10

    """)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        print(result["article"]["value"])

    print('---------------------------')


def searchArticleTitle():
    print("Ingrese el titulo del articulo")
    titulo = input()

    sparql = SPARQLWrapper("http://localhost:7200/repositories/covid19_sbc")
    sparql.setQuery("""
            PREFIX dct: <http://purl.org/dc/terms/>
            PREFIX vivo: <http://vivoweb.org/ontology/core#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX bibo: <http://purl.org/ontology/bibo/>
            
            select ?s ?title ?url where {
                values ?keyword{'""" + titulo + """'}
                ?s rdf:type vivo:Article .
                ?s dct:title ?title .
                ?s bibo:uri ?url
                OPTIONAL{?s bibo:abstract ?abstract. }
                FILTER(REGEX(?title, ?keyword))
            }
    """)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    for result in results["results"]["bindings"]:
        print("URI: " + result["s"]["value"])
        print("Titulo: " + result["title"]["value"])
        print("URL: " + result["url"]["value"])
        print('---------------------------')

    main()


def searchArticleAuthor():
    print("Ingrese el autor del cual desea buscar los articulos")
    autor = input()

    sparql = SPARQLWrapper("http://localhost:7200/repositories/covid19_sbc")
    sparql.setQuery("""
                PREFIX dct: <http://purl.org/dc/terms/>
                PREFIX vivo: <http://vivoweb.org/ontology/core#>
                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                PREFIX bibo: <http://purl.org/ontology/bibo/>
                PREFIX dc: <http://purl.org/dc/terms/>
                PREFIX foaf: <http://xmlns.com/foaf/0.1/>
                
                select ?s ?title ?name ?url where {
                    values ?keyword{'""" + autor + """'}
                    ?s rdf:type vivo:Article .
                    ?s dct:title ?title .
                    ?s bibo:uri ?url .
                    ?s dc:creator ?author .
                    ?author foaf:name ?name .
                    FILTER(REGEX(?name, ?keyword))
                }
        """)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    for result in results["results"]["bindings"]:
        print("URI: " + result["s"]["value"])
        print("Titulo: " + result["title"]["value"])
        print("Autor: " + result["s"]["value"])
        print("URL: " + result["url"]["value"])
        print('---------------------------')

    main()


def searchArticleFieldStudy():
    print("Ingrese el campo de estudio del cual desea buscar los articulos")
    field = input()

    sparql = SPARQLWrapper("http://localhost:7200/repositories/covid19_sbc")
    sparql.setQuery("""
                    PREFIX dct: <http://purl.org/dc/terms/>
                    PREFIX vivo: <http://vivoweb.org/ontology/core#>
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                    PREFIX bibo: <http://purl.org/ontology/bibo/>
                    PREFIX dc: <http://purl.org/dc/terms/>
                    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
                    PREFIX skos: <http://www.w3.org/2004/02/skos/core#/>
                    
                    select ?s ?title ?url where {
                        values ?keyword{'""" + field + """'}
                        ?s rdf:type vivo:Article .
                        ?s dct:title ?title .
                        ?s bibo:uri ?url .
                        ?s dc:subject ?mentions .
                        ?mentions skos:prefLabel ?keyword .

                    }
            """)
    resultados = 0
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    for result in results["results"]["bindings"]:
        print("URI: " + result["s"]["value"])
        print("Titulo: " + result["title"]["value"])
        print("URL: " + result["url"]["value"])
        print('---------------------------')
        resultados = resultados + 1

    print("Número de resultados: " + str(resultados) + "\n\n\n")

    main()


def consultaPre1():
    sparql = SPARQLWrapper("http://localhost:7200/repositories/covid19_sbc")
    sparql.setQuery("""
                        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
                        PREFIX vivo: <http://vivoweb.org/ontology/core#>
                        PREFIX bibo: <http://purl.org/ontology/bibo/>
                        PREFIX journalArticle: <http://utpl.edu.ec/sbc/>
                        PREFIX dct: <http://purl.org/dc/terms/>
                        PREFIX dc: <http://purl.org/dc/terms/>
                        PREFIX skos: <http://www.w3.org/2004/02/skos/core#/>
                        
                        SELECT DISTINCT ?art ?title ?doi ?nom ?url
                        WHERE { 
                            values ?keyword{"Medicine"}
                            ?art rdf:type vivo:Article .
                            ?art dct:date ?date .
                            ?art bibo:doi ?doi .
                            ?art dc:title ?title .
                            ?art bibo:uri ?url .
                            ?art dc:subject ?mentions .
                            ?mentions skos:prefLabel ?keyword .
                            ?art dc:creator ?author .
                            ?author foaf:name ?nom .
                            FILTER (?date = "2021") .
                        }
                """)
    resultados = 0
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    for result in results["results"]["bindings"]:
        print("URI: " + result["art"]["value"])
        print("Titulo: " + result["title"]["value"])
        print("DOI: " + result["doi"]["value"])
        print("Autor: " + result["nom"]["value"])
        print("URL: " + result["url"]["value"])
        print('---------------------------')
        resultados = resultados + 1

    print("Número de resultados: " + str(resultados) + "\n\n\n")

    main()


def consultaPre2():
    sparql = SPARQLWrapper("http://localhost:7200/repositories/covid19_sbc")
    sparql.setQuery("""
                            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                            PREFIX vivo: <http://vivoweb.org/ontology/core#>
                            PREFIX bibo: <http://purl.org/ontology/bibo/>
                            PREFIX journalArticle: <http://utpl.edu.ec/sbc/>
                            PREFIX dct: <http://purl.org/dc/terms/>
                            PREFIX skos: <http://www.w3.org/2004/02/skos/core#/>
                            
                            SELECT DISTINCT ?art ?nom ?Cat ?date ?url
                            WHERE { 
                                ?art rdf:type vivo:Article .
                                ?art dct:title ?nom .
                                ?art bibo:uri ?url .
                                ?suj skos:prefLabel ?Cat .
                                ?art dct:date ?date .
                                FILTER(?Cat != "Medicine") .
                                 FILTER(?date >"2017" && ?date <"2021") .
                            }
                    """)
    resultados = 0
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    for result in results["results"]["bindings"]:
        print("URI: " + result["art"]["value"])
        print("Titulo: " + result["nom"]["value"])
        print("Categoria: " + result["Cat"]["value"])
        print("Fecha: " + result["date"]["value"])
        print("URL: " + result["url"]["value"])
        print('---------------------------')
        resultados = resultados + 1

    print("Número de resultados: " + str(resultados) + "\n\n\n")

    main()


def consultaPre3():
    sparql = SPARQLWrapper("http://localhost:7200/repositories/covid19_sbc")
    sparql.setQuery("""
                                PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                                PREFIX vivo: <http://vivoweb.org/ontology/core#>
                                PREFIX bibo: <http://purl.org/ontology/bibo/>
                                PREFIX journalArticle: <http://utpl.edu.ec/sbc/>
                                PREFIX dct: <http://purl.org/dc/terms/>
                                
                                SELECT ?s ?title ?url
                                WHERE{
                                VALUES ?keyword {"Vaccine"}
                                    ?s rdf:type vivo:Article .
                                    ?s dct:title ?title .
                                    ?s bibo:uri ?url .
                                OPTIONAL {?s bibo:abstract ?abstract. }
                                FILTER (REGEX (?title, ?keyword) || REGEX (?abstract, ?keyword))
}
                        """)
    resultados = 0
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    for result in results["results"]["bindings"]:
        print("URI: " + result["s"]["value"])
        print("Titulo: " + result["title"]["value"])
        print("URL: " + result["url"]["value"])
        print('---------------------------')
        resultados = resultados + 1

    print("Número de resultados: " + str(resultados) + "\n\n\n")

    main()


def searchArticleKey():
    print("Ingrese la parabla clave")
    key = input()

    sparql = SPARQLWrapper("http://localhost:7200/repositories/covid19_sbc")
    sparql.setQuery("""
                        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
                        PREFIX vivo: <http://vivoweb.org/ontology/core#>
                        PREFIX bibo: <http://purl.org/ontology/bibo/>
                        PREFIX journalArticle: <http://utpl.edu.ec/sbc/>
                        PREFIX dct: <http://purl.org/dc/terms/>
                        PREFIX schema: <http://schema.org/>
                                                        
                        SELECT ?s ?title ?url
                        WHERE{
                        VALUES ?keyword {'"""+key+"""'}
                        ?s rdf:type vivo:Article .
                        ?s dct:title ?title .
                        ?s bibo:uri ?url .
                        ?s schema:mentions ?m .
                        OPTIONAL {?m rdf:label ?mentions.}
                        FILTER (REGEX (?title, ?keyword) || REGEX (?mentions, ?keyword))
                        }

                """)
    resultados = 0
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    for result in results["results"]["bindings"]:
        print("URI: " + result["s"]["value"])
        print("Titulo: " + result["title"]["value"])
        print("URL: " + result["url"]["value"])
        print('---------------------------')
        resultados = resultados + 1

    print("Número de resultados: " + str(resultados) + "\n\n\n")

    main()


def main():
    print("Seleccione un número\n\n")
    print("1. Modelos de consultas pre elaboradas")
    print("2. Buscar articulos por titulo")
    print("3. Buscar articulos por autor")
    print("4. Buscar articulos por campo de estudio")
    print("5. Buscar articulos por palabras clave")
    print("X. Salir")

    opcion = input()

    if opcion == "1":
        print("1. ¿Cuales son los artículos pertenecientes al área de Medicina que han sido creados en el año 2021 y cual es su doi y autor?")
        print("2. ¿Cuáles son los artículos cuya categoría pertenecen únicamente al área de Medicina y que son mayores al año 2017 y menores al año 2021?")
        print("3. ¿Cuáles son los nombres de los artículos que tienen en el título o el abstract la palabra “Vaccine”?")

        seleccion = input()

        if seleccion == "1":
            consultaPre1()

        if seleccion == "2":
            consultaPre2()

        if seleccion == "3":
            consultaPre3()

    if opcion == "2":
        searchArticleTitle()

    if opcion == "3":
        searchArticleAuthor()

    if opcion == "4":
        searchArticleFieldStudy()

    if opcion == "5":
        searchArticleKey()

    if opcion == "X":
        pass


if __name__ == '__main__':
    print("Bienvenido al sistema de Buscador Semantico\n")
    print("-------------------------------------------\n\n")
    main()
