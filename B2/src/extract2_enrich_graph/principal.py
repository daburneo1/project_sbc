import pickle

import semantic_annotation
from modelado.modelo import *
from data.DataBase import *


def getLabel(a):
    list = a.split("/")
    label = list[-1]
    return label


def create_triples(idArticle, mentions, categories):
    triples_mention = []
    mention_type = []
    triples_subject = []
    triples = []

    for a in mentions:
        triples_mention = idArticle + " schema:mentions " + "<" + a + ">" + " ."
        mention_type = "<" + a + ">" + " rdfs:label " + "'" + getLabel(a) + "' ."
        triples.append(triples_mention)
        triples.append(mention_type)

    for b in categories:
        triples_subject = idArticle + " dct:subject " + "<" + b + ">" + " ."
        triples.append(triples_subject)

    print(triples)
    return (triples)


def create_abstract(Articles):
    mentions = []
    categories = []
    triples = []
    for x in Articles:
        print(x.get_id())
        if x.get_abstract() != None:
            dbCategories = semantic_annotation.getAnnotationsAbstract(x.get_paperId(), x.get_abstract())
            for a in dbCategories:
                mentions.append(a[0])
                categories.append(a[1])
            mentions = list(set(mentions))
            categories = list(set(categories))
            # print(mentions)
            # print(categories)
            idArticle = x.get_paperId()

            triples.append(create_triples(idArticle, mentions, categories))

    result = []
    for item in triples:
        for item2 in item:
            if item2 not in result:
                result.append(item2)

    with open('tripletas.rdf', 'w') as temp_file:
        for item in result:
                temp_file.write("%s\n" % item)


def create_object_article(tupla, fieldStudy):
    objArticle = Journal_Article(
        tupla[0], tupla[1], tupla[2],
        tupla[3], tupla[4], tupla[5],
        tupla[6], tupla[7], tupla[8],

        tupla[9], fieldStudy
    )
    return objArticle


def get_articles_data_base():
    inst = DataBase()
    Articles = []
    for i in range(1495):  # 1496
        objArticle = inst.get_article(i + 1)
        idArticle = objArticle[0]
        fieldStudy = inst.get_field_study(idArticle)
        if fieldStudy is None:
            fieldStudy = None
        else:
            fieldStudy = fieldStudy[0]
        objArticle = create_object_article(objArticle, fieldStudy)
        print(objArticle)
        Articles.append(objArticle)
    return Articles


def create_field_study(Articles):
    for x in Articles:
        if x.get_fieldsOfStudy() != None:
            dbCategories = semantic_annotation.getAnnotations(x.get_paperId(), x.get_fieldsOfStudy())
            for a in dbCategories:
                print(40 * '-')
                print(a)  # DBpedia categories


def create_venue(Articles):
    for x in Articles:
        if x.get_venue() != None:
            dbCategories = semantic_annotation.getAnnotations(x.get_paperId(), x.get_venue())
            for a in dbCategories:
                print(40 * '-')
                print(a)  # DBpedia categories


def main():
    Articles = get_articles_data_base()

    print("1 - Abstract\n"
          "2 - Venue\n"
          "3 - Field of Study")

    option = input()

    if option == '1':
        create_abstract(Articles)

    if option == '2':
        create_venue(Articles)

    if option == '3':
        create_field_study(Articles)


if __name__ == '__main__':
    main()
