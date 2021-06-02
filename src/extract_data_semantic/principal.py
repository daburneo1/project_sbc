from modelado.modelo import *
from data.DataBase import *
import semanticscholar as sch
from crossref.restful import Works
import time

def registerArticle(paper):
    container_paper = {
        'abstract': '',
        'citationVelocity': '',
        'corpusId': '',
        'doi': '',
        'fieldsOfStudy': '',
        'isOpenAccess': '',
        'isPublisherLicensed': '',
        'numCitedBy': '',
        'numCiting': '',
        'paperId': '',
        'url': '',
        'title': '',
        'year': 0,
        'authors':[],
        'references':[]
    }

    author_list = []
    references_list = []
    for key in container_paper.keys():
        if key in list(paper.keys()):
            if key == 'authors':
                for i in paper['authors']:
                    author_list.append(i)
                paper[key] = create_authors(author_list)
            if key == 'references':
                for j in paper['references']:
                    references_list.append(j)
                paper[key] = create_references(references_list)
            container_paper[key] = paper[key]
    return create_article(container_paper)


def create_article(paper):
    objPaper = Journal_Article(
        paper['abstract'], paper['citationVelocity'], paper['corpusId'],
        paper['doi'], paper['fieldsOfStudy'], paper['isOpenAccess'], paper['isPublisherLicensed'],
        paper['numCitedBy'], paper['numCiting'], paper['paperId'], paper['title'], paper['url'],
        paper['year'], paper['authors'], paper['references']
    )

    print(objPaper)

    inst = DataBase()
    exist = inst.find_article(objPaper)
    if exist == True:
        inst.insert_journal(objPaper)
        idJournal = inst.get_id_journal(objPaper)
        inst.insert_references(objPaper, idJournal)
        inst.insert_authors(objPaper, idJournal)
        if(objPaper.get_fieldsOfStudy() != None):
            inst.insert_fieldsOfStudy(objPaper, idJournal)

def create_authors(authors):
    authors_list = []
    for i in authors:
        a = sch.author(i['authorId'], timeout=10)
        if 'authorId' in list(a.keys()):
            objAutor = Author(a['authorId'], a['name'], a['url'],
                               a['influentialCitationCount'], a['aliases'])
            authors_list.append(objAutor)
    return authors_list

def create_references(references):
    references_list = []
    for i in references:
        objReference = Reference(i['doi'], i['title'], i['year'], i['isInfluential'], i['arxivId'])
        references_list.append(objReference)

    return references_list


def main():
    a = 1
    sleeps = 20 #cambiar a 20
    works = Works()
    w1 = works.query(bibliographic='covid-19 vaccine thrombosis')\
        .filter(type='journal-article', from_pub_date='2021')\
        .sort('relevance')\
        .select('DOI')
    c = 0
    for article in w1:
        c = c + 1
        print(c, ' ', article)
        if c > 0:
            contador = 0
            bool = False
            while bool == False:
                paper = sch.paper(article['DOI'], timeout=10)
                if 'title' in paper:
                    registerArticle(paper)
                    a = a + 1
                    print(a)
                    bool = True
                    break
                else:
                    print('waiting %s' % contador)
                    time.sleep(sleeps)
                    bool = False
                    contador = contador + 1
                    if contador > 2:
                        bool = True
                        break

if __name__ == '__main__':
    main()
