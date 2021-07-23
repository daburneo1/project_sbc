class Journal_Article(object):
    def __init__(self, id, abstract, doi, isOpenAccess, numCiting, paperId, title, venue,
                 url, year, fieldsOfStudy):
        self.id = id
        self.abstract = abstract
        self.doi = doi
        self.isOpenAcces = isOpenAccess
        self.numCiting = numCiting
        self.paperId = paperId
        self.title = title
        self.venue = venue
        self.url = url
        self.year = year
        self.fieldsOfStudy = fieldsOfStudy

    def get_id(self):
        return self.id

    def get_abstract(self):
        return self.abstract

    def get_doi(self):
        return self.doi

    def get_venue(self):
        return self.venue

    def get_fieldsOfStudy(self):
        return self.fieldsOfStudy

    def get_isOpenAccess(self):
        return self.isOpenAcces

    def get_numCiting(self):
        return self.numCiting

    def get_paperId(self):
        return self.paperId

    def get_url(self):
        return self.url

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    def __repr__(self):
        return str(self.__dict__)


class Author(object):
    def __init__(self, Id, name, url, influentialCitationCount, aliases):
        self.Id = Id
        self.name = name
        self.url = url
        self.influentialCitationCount = influentialCitationCount
        self.aliases = aliases

    def get_authorId(self):
        return self.Id

    def get_name(self):
        return self.name

    def get_url(self):
        return self.url

    def get_influentialCitationCount(self):
        return self.influentialCitationCount

    def get_aliases(self):
        return self.aliases

    def __repr__(self):
        return str(self.__dict__)

class Reference(object):
    def __init__(self, doi, title, year, isInfluential):
        self.doi = doi
        self.title = title
        self.year = year
        self.isInfluential = isInfluential

    def get_doi(self):
        return self.doi

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    def get_isInfluential(self):
        return self.isInfluential

    def __repr__(self):
        return str(self.__dict__)

