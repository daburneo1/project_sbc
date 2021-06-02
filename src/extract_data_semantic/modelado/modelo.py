class Journal_Article(object):
    def __init__(self, abstract, citationVelocity, corpusId, doi, fieldsOfStudy, isOpenAcces, isPublisherLicensed, numCitedBy,
                 numCiting, paperId, title, url, year, authors, references):
        self.abstract = abstract
        self.citationVelocity = citationVelocity
        self.corpusId = corpusId
        self.doi = doi
        self.fieldsOfStudy = fieldsOfStudy
        self.isOpenAcces = isOpenAcces
        self.isPublisherLicensed = isPublisherLicensed
        self.numCitedBy = numCitedBy
        self.numCiting = numCiting
        self.paperId = paperId
        self.url = url
        self.title = title
        self.year = year
        self.authors = authors
        self.references = references


    def get_abstract(self):
        return self.abstract

    def get_references(self):
        return self.references

    def get_citationVelocity(self):
        return self.citationVelocity

    def get_corpusId(self):
        return self.corpusId

    def get_doi(self):
        return self.doi

    def get_fieldsOfStudy(self):
        return self.fieldsOfStudy

    def get_isOpenAccess(self):
        return self.isOpenAcces

    def get_isPublisherLicenced(self):
        return self.isPublisherLicensed

    def get_numCitedBy(self):
        return self.numCitedBy

    def get_numCiting(self):
        return self.numCiting

    def get_paperId(self):
        return self.paperId

    def get_url(self):
        return self.url

    def get_title(self):
        return self.title

    def get_authors(self):
        return self.authors

    def get_year(self):
        return self.year

    def __repr__(self):
        return str(self.__dict__)


class Author(object):
    def __init__(self, authorId, name, url, influentialCitationCount, aliases):
        self.authorId = authorId
        self.name = name
        self.url = url
        self.influentialCitationCount = influentialCitationCount
        self.aliases = aliases

    def get_authorId(self):
        return self.authorId

    def get_name(self):
        return self.name

    def get_url(self):
        return self.url

    def get_influentialCitationCount(self):
        return self.influentialCitationCount

    def get_aliases(self):
        return self.aliases

    def get_papers(self):
        return self.papers

    def __repr__(self):
        return str(self.__dict__)

class Reference(object):
    def __init__(self, doi, title, year, isInfluential, arxivId):
        self.doi = doi
        self.title = title
        self.year = year
        self.isInfluential = isInfluential
        self.arxivId = arxivId

    def get_doi(self):
        return self.doi

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    def get_isInfluential(self):
        return self.isInfluential

    def get_arxivId(self):
        return self.arxivId

    def __repr__(self):
        return str(self.__dict__)

